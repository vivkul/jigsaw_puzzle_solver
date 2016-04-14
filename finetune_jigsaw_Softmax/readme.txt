It is finetuning of bvlc_reference_caffenet (which is slight modification of AlexNet) with output being 24 classes instead of 1000.

The input dimention of images is 227x227x3.

To run the model, use the following from caffe-root directory:
./build/tools/caffe train -solver models/finetune_jigsaw_Softmax/solver.prototxt -weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0
