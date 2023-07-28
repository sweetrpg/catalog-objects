from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-catalog-objects",
    install_requires=[
        "Flask~=2.0",
        "marshmallow-jsonapi~=3.20",
        "mongoengine~=0.27",
        "sweetrpg-api-core",
        "sweetrpg-db",
        "sweetrpg-model-core",
    ],
)
