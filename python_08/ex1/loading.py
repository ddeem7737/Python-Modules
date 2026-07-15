import sys
import importlib
import importlib.util
import importlib.metadata


def check_package() -> bool:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }
    res = True

    for package, message in packages.items():
        spec = importlib.util.find_spec(package)
        if spec is None:
            print(f"[MISSING] {package}")
            res = False
        else:
            print(f"[OK] {package} "
                  f"({importlib.metadata.version(package)}) - {message}")

    return res


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    if not check_package():
        print("To install dependencies:")
        print("With pip:    pip install -r requirements.txt")
        print("With Poetry: poetry install")
        sys.exit(1)

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    table = pd.DataFrame(data, columns=["value"])
    print("Generating visualization...")
    fig, ax = plt.subplots()
    ax.hist(table["value"], bins=50, color="green")
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    print()
    print("Dependency Management Differences:")
    print("pip:    Relies on requirements.txt, installed globally "
          "or in current env.")
    print("Poetry: Uses pyproject.toml, automatically manages virtual "
          "environments and strict dependency resolution.")


if __name__ == "__main__":
    main()
