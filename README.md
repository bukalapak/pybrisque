# PyBRISQUE
An implementation of BRISQUE (Blind/Referenceless Image Spatial Quality 
Evaluator) in Python from the paper: ["No-Reference Image Quality Assessment 
in the Spatial Domain"](https://ieeexplore.ieee.org/document/6272356/).


## Installation

## Installing libsvm
LibSVM and its python bindings are required. Please ensure that the libsvm library and its python bindings are compatible with each other (even better, having the exact same version). On ubuntu or other debian-based system, you can install ```libsvm-dev``` package from apt as follows:

```apt-get install libsvm-dev```

As a note, libsvm version on debian package list is as follows:
- Ubuntu 16.04: 3.12
- Ubuntu 18.04: 3.21

If you're on debian, you can install its python binding with the exact same version by running:
```apt-get install python-libsvm```. Please be aware that the binding is only linked to Python 2.7. You can manually link them to your currently active environment by adding it to your PYTHONPATH or your sys path as such:
```
>> import sys
>>> sys.path.append('/usr/share/pyshared')
```


If you're using macOS, using brew, you can have the latest version (3.23). See [here](https://github.com/Homebrew/homebrew-core/blob/master/Formula/libsvm.rb).

## Installing pybrisque
The package is in PyPI so you can install it simply by this command:

```pip install pybrisque```

## Usage
Initialize once:
```
brisq = BRISQUE()
```
and get the BRISQUE feature or score many times:
```
brisq.get_feature('/path')
brisq.get_score('/image_path')
```


## Limitations
This implementation is heavily adopted from the original Matlab 
implementation in [here](https://github.com/dsoellinger/blind_image_quality_toolbox/tree/master/%2Bbrisque). There is one catch though, the bicubic interpolation when resizing image in 
Matlab and OpenCV is a bit different as explained in [here](https://stackoverflow.com/questions/26823140/imresize-trying-to-understand-the-bicubic-interpolation). For now, it uses ```nearest``` interpolation 
which gives the most similar output with the original implementation.

Comparing with Matlab original implementation on reference images of TID 2008: 

![Comparison](examples/comparison.png)
 
And the absolute differences' stat is as follows: 
```
{'min': 0.17222238726479588,
 'max': 16.544924728934404,
 'mean': 3.9994322498322754,
 'std': 3.0715344507521416}
```


