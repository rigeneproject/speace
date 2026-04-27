from setuptools import setup, find_packages

setup(
    name="speace_core",
    version="0.3.0",
    packages=find_packages(),
    install_requires=["networkx>=3.3", "numpy"],
    python_requires=">=3.10",
    description="SPEACE Core Graph Engine - Cervello Digitale",
    author="Grok + Team SPEACE"
)