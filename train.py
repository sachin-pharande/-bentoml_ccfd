import xgboost as xgb
import pandas as pd
import bentoml
import warnings

warnings.filterwarnings("ignore")


def train_xgb_save(X, y, tag_name="xgb_final"):
    """
    A simple function to train a model and save it to BentoML model store.
    """
    # Create DMatrix
    dtrain = xgb.DMatrix(X.values, label=y.values)
    # Specify parameters for a binary classification problem
    params = {"objective": "binary:logistic", "booster": "gbtree", "eval_metric": "auc"}

    # Train
    booster = xgb.train(params=params, dtrain=dtrain, num_boost_round=20)

    bentoml.xgboost.save_model("xgb_initial", booster)

    bentoml.xgboost.save_model("xgb_custom",booster,
    metadata={"auc": 0.99, 
              "feature_importances": booster.get_score(importance_type="gain")},
    labels={"author": "MLops"},)
    

if __name__ == "__main__":
    # Load and prep the data
    data = pd.read_csv("Final_df.csv")
    X, y = data.drop("IsDefaulter", axis=1), data[["IsDefaulter"]]

    # Train and save
    train_xgb_save(X, y, "xgb_booster")
