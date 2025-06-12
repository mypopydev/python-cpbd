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

# 读取灰度图像
input_image = imread('your_image.jpg', as_gray=True)

# 计算清晰度
sharpness = cpbd.compute(input_image)
print(f"CPBD sharpness score: {sharpness}")
```

## Development

```bash
git clone https://github.com/0x64746b/python-cpbd.git
cd python-cpbd
pip install -e ".[dev]"
```

### Running Tests

项目包含完整的测试套件，使用 pytest 运行。测试数据来自原始 MATLAB 实现，确保 Python 端口的结果与参考实现一致。

#### 运行所有测试

```bash
pytest
```

#### 运行特定测试文件

```bash
pytest tests/test_compute.py
```

#### 显示详细测试信息

```bash
pytest -vv --tb=long -s
```

测试选项说明：
- `-vv`: 显示详细输出
- `--tb=long`: 显示完整的错误回溯
- `-s`: 显示打印输出
- `--durations=0`: 显示所有测试的耗时

#### 测试内容

测试套件包含以下主要测试：
1. `test_marziliano_method`: 验证 Marziliano 方法计算边缘宽度的准确性
2. `test_calculate_sharpness_metric`: 验证清晰度指标计算的准确性

测试数据存储在 `tests/data/` 目录下，包括：
- 参考图像数据
- Sobel 边缘检测结果
- Canny 边缘检测结果
- Marziliano 宽度结果

## Performance

The following graph visualizes the accuracy of this port in comparison with the reference implementation when tested on the [images](http://lina.faculty.asu.edu/Software/CPBDM/LIVE_Images_GBlur.zip) of the [LIVE database](http://live.ece.utexas.edu/research/quality/subjective.htm):

![Performance on LIVE database](https://raw.githubusercontent.com/0x64746b/python-cpbd/master/tests/data/performance_LIVE.png) 