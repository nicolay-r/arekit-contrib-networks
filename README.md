# arekit-contrib-networks
![](https://img.shields.io/badge/Python-3.9-brightgreen.svg)
![](https://img.shields.io/badge/AREkit-0.25.1-orange.svg)


> **NOTE:** This code base is a  **contrib** part from the [AREkit-0.25.0 release](https://github.com/nicolay-r/AREkit/releases/tag/v0.25.0-rc).

This project represent code part that has been related to 
**serialization of data** necessary for 🧪**experiments with neural networks** 🤖 in the domain of 
**attitudes and relation extraction**.
This project is powered by [AREkit pipelines](https://github.com/nicolay-r/AREkit).

In particular, the most crucial part of this project is 
* `NetworksInputSerializerPipelineItem` -- represent a pipeline element for handy data serialization that involves:
    * Embedding preparation;
    * Tokenization;
    * Annotation of entities;
    * Annotation of subject-object pairs.

## Third-party projects

The projects that depend on the related source code but not directly depends on from the PyPI are: 
* ### [arekit-ss](https://github.com/nicolay-r/arekit-ss): supports serialization for neural networks from various sources
* ### [AREnets](https://github.com/nicolay-r/AREnets): supports traning launching using Tensorflow API

## Powered by

* AREkit [[github]](https://github.com/nicolay-r/AREkit)

<p float="left">
<a href="https://github.com/nicolay-r/AREkit"><img src="https://github.com/nicolay-r/ARElight/assets/14871187/01232f7a-970f-416c-b7a4-1cda48506afe"/></a>
</p>

## How to cite

```bibtex
@inproceedings{rusnachenko2024arelight,
  title={ARElight: Context Sampling of Large Texts for Deep Learning Relation Extraction},
  author={Rusnachenko, Nicolay and Liang, Huizhi and Kolomeets, Maxim and Shi, Lei},
  booktitle={European Conference on Information Retrieval},
  year={2024},
  organization={Springer}
}
```