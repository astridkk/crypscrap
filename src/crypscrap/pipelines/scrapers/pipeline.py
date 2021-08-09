from kedro.pipeline import Pipeline, node
from .nodes import crypcur_scraper

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=crypcur_scraper,
                inputs=None,
                outputs="crypcur",
                name="crypcur_scraper_node",
            ),
        ]
    )