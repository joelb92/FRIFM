# Python FRIFM

FRIFM (Facial Region In Focus Measure) is a simple yet effective way to measure the quality of a face capture within an image.
More information can be found [here](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=890059)



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:

```bash
pip install numpy
pip install dlib
pip install skimage
```

## Usage in Terminal or Command Line
```bash
python3 FRIFM.py <image path>
```
##Usage in Python
```python
import FRIFM

impath="/path/to/image.jpg"

FRIFM_scores = runFRIFM(impath)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)