# beamCalculator
A simple GUI application for 2D engineering analysis of beam models. Users can calculate the max bending moment, shear force, and deflection of a custom 2D beam model.
Users also have the ability to display and save labeled free body diagrams, bending moment plots, shear force plots, and deflection plots. 

## What I Learned
* Objected Oriented Programming with Python
* GUI Development using [PyQt](https://doc.qt.io/qtforpython/) and [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
* Unit testing GUI's with [PyTest](https://docs.pytest.org/en/7.0.x/)
## Features
* Allows users to create a customised 2D beam model
  * users can specify beam length
  * users can specify force location
  * users can specify joint location
  * supports point loads and UDL's
  * supports cantilever, roller and pin joints
  * supports AISI-1045 Steel and Cast Iron Grade20 materials 
  * supports both solid and hollow cross-sections
  * supports square and circulr cross sections
* Save Free body, bending moment, shear force and deflection plots for use in an engineering report
## Example Usage (currently still in development)
```python
python3 Ui/beam_calculator_main_window.py
```
### Enter cross-section type, dimensions and material
![alt text](https://github.com/mark2661/beamCalculator/blob/main/images/main_window.png)
### Click "Add beam" and enter overall beam length
![alt text](https://github.com/mark2661/beamCalculator/blob/main/images/add_beam_dialog.png)
### Add supports
![alt text](https://github.com/mark2661/beamCalculator/blob/main/images/add_support_dialog_window.png)
### Add loading details
![alt text](https://github.com/mark2661/beamCalculator/blob/main/images/point_load_dialog.png)
### Solve
![alt text](https://github.com/mark2661/beamCalculator/blob/main/images/results.png)
### Click "Generate Report"
![alt text](https://github.com/mark2661/beamCalculator/blob/main/images/report.png)

## Future Updates
* Add a preview window which shows a simple 2D sketch of the current state of the user beam
* Add a material database with a custom API
* Add support for non-uniform distributed loads
