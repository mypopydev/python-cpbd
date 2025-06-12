# CPBD

CPBD is a perceptual-based no-reference objective image sharpness metric based on the cumulative probability of blur detection [developed at the Image, Video and Usability Laboratory of Arizona State University](https://ivulab.asu.edu/Quality/CPBD).

> [The metric] is based on the study of human blur perception for varying contrast values. The metric utilizes a probabilistic model to estimate the probability of detecting blur at each edge in the image, and then the information is pooled by computing the cumulative probability of blur detection (CPBD).

This software is a Python port of the [reference MATLAB implementation](http://lina.faculty.asu.edu/Software/CPBDM/CPBDM_Release_v1.0.zip). To approximate the behaviour of MATLAB's proprietary implementation of the Sobel operator, it uses an implementation [inspired by GNU Octave](https://sourceforge.net/p/octave/image/ci/default/tree/inst/edge.m#l196).

## References

CPBD is described in detail in the following papers:

- N. D. Narvekar and L. J. Karam, "A No-Reference Image Blur Metric Based on the Cumulative Probability of Blur Detection (CPBD)," in IEEE Transactions on Image Processing, vol. 20, no. 9, pp. 2678-2683, Sept. 2011. [link](http://ieeexplore.ieee.org/abstract/document/5739529/)
- N. D. Narvekar and L. J. Karam, "An Improved No-Reference Sharpness Metric Based on the Probability of Blur Detection," International Workshop on Video Processing and Quality Metrics for Consumer Electronics (VPQM), January 2010, [pdf](http://events.engineering.asu.edu/vpqm/vpqm10/Proceedings_VPQM2010/vpqm_p27.pdf)
- N. D. Narvekar and L. J. Karam, "A no-reference perceptual image sharpness metric based on a cumulative probability of blur detection," 2009 International Workshop on Quality of Multimedia Experience, San Diego, CA, 2009, pp. 87-91. [link](http://ieeexplore.ieee.org/abstract/document/5246972/)

## Credits

If you publish research results using this code, please reference the papers of the original authors of the metric as stated in the previous section as well as their reference implementation in your bibliography. See also the copyright statement of the reference implementation in the [LICENSE.txt](LICENSE.txt) file. Thank you!

## Installation

```bash
pip install cpbd
```

## Usage

```python
import cpbd
from imageio import imread

# Read grayscale image
input_image = imread('your_image.jpg', as_gray=True)

# Calculate sharpness
sharpness = cpbd.compute(input_image)
print(f"CPBD sharpness score: {sharpness}")
```

## Development

```bash
git clone https://github.com/mypopydev/python-cpbd.git
cd python-cpbd
pip install -e ".[dev]"
```

### Running Tests

The project includes a complete test suite using pytest. The test data comes from the original MATLAB implementation to ensure the Python port produces results consistent with the reference implementation.

#### Run All Tests

```bash
pytest
```

#### Run Specific Test File

```bash
pytest tests/test_compute.py
```

#### Show Detailed Test Information

```bash
pytest -vv --tb=long -s
```

Test options explanation:
- `-vv`: Show verbose output
- `--tb=long`: Show full error traceback
- `-s`: Show print output
- `--durations=0`: Show timing for all tests

#### Test Contents

The test suite includes the following main tests:
1. `test_marziliano_method`: Validates the accuracy of edge width calculation using the Marziliano method
2. `test_calculate_sharpness_metric`: Validates the accuracy of the sharpness metric calculation

Test data is stored in the `tests/data/` directory, including:
- Reference image data
- Sobel edge detection results
- Canny edge detection results
- Marziliano width results

## Performance

The following graph visualizes the accuracy of this port in comparison with the reference implementation when tested on the [images](http://lina.faculty.asu.edu/Software/CPBDM/LIVE_Images_GBlur.zip) of the [LIVE database](http://live.ece.utexas.edu/research/quality/subjective.htm):

![Performance on LIVE database](https://raw.githubusercontent.com/mypopydev/python-cpbd/master/tests/data/performance_LIVE.png) 