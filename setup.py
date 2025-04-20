from setuptools import setup, find_packages

setup(
    name="quantum_simulator",  # Package name
    version="0.1.0",  # Package version
    packages=find_packages(),  # Automatically find all packages in the quantum_simulator folder
    install_requires=[  # List of dependencies
        "numpy",  # Required package
        "matplotlib",  # Required package for plotting
    ],
    entry_points={  # CLI entry point to run the simulation
        'console_scripts': [
            'quantum-simulator = quantum_simulator.main:main',  # Run `python -m quantum_simulator.main` from CLI
        ],
    },
    classifiers=[  # Additional metadata for the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  #  supported Python versions
)
