from setuptools import setup, find_packages

setup(
    name="AlgoritmoGeneticoUdeC-Base",
    version="0.2.0",
    description="Un proyecto base para algoritmos genéticos en Python.",
    url="https://github.com/Juan9Walteros/AlgoritmosGeneticos_Base.git",
    author="Juan Walteros",
    author_email="juan9walteros@gmail.com",
    license="MIT",  # Asegúrate de especificar una licencia válida
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pygad"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
