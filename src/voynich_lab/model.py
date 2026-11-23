"""XGBoost süreç sınıflandırıcısı: gruplu çapraz doğrulama ve nihai eğitim."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GroupKFold
from xgboost import XGBClassifier

from .features import FEATURE_NAMES


def _new_model(seed: int) -> XGBClassifier:
    return XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=seed,
        n_jobs=4,
        eval_metric="mlogloss",
    )


def _encode(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, list[str]]:
    classes = sorted(df["label"].unique())
    y = df["label"].map({c: i for i, c in enumerate(classes)}).to_numpy()
    return df[FEATURE_NAMES].to_numpy(dtype=float), y, classes


def cross_validate(df: pd.DataFrame, n_splits: int = 5, seed: int = 7) -> dict:
    """Grupları (dilleri) bütün olarak dışarıda bırakan çapraz doğrulama."""
    X, y, classes = _encode(df)
    pred = np.empty_like(y)
    for train, test in GroupKFold(n_splits=n_splits).split(X, y, df["group"]):
        pred[test] = _new_model(seed).fit(X[train], y[train]).predict(X[test])
    cm = confusion_matrix(y, pred, labels=range(len(classes)))
    return {
        "accuracy": float(accuracy_score(y, pred)),
        "classes": classes,
        "confusion_matrix": cm.tolist(),
        "per_class_recall": {
            c: float(cm[i, i] / cm[i].sum()) for i, c in enumerate(classes)
        },
    }


def fit(df: pd.DataFrame, seed: int = 7) -> tuple[XGBClassifier, list[str]]:
    X, y, classes = _encode(df)
    return _new_model(seed).fit(X, y), classes
