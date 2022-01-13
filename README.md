<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

# Weed-Detection
  
The main objective of the ```Weed-Detection``` module is to provide a more thorough inspection on problematic areas, as have been extracted from the [```Problematic-Areas-Detection```](https://github.com/CoFly-Project/Problematic-Areas-Detection) module in terms of plant health and provide valuable information to the end-user. In specific, the developed module is based on the pretrained DeepLabv3+ instance was pretrained on PASCAL VOC 2012 dataset and further trained on the  [```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB) dataset for the weed semantic segmentation task. The developed module is capable of semantically segmenting weed instances depicted on input RGB images and thus, provides accurate information regarding the location of detected weeds.
  
Concerning about the training and evaluation of the detector, the developed dataset ([```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB)) was split to a training (80%) and a testing (20%) set where depicted weed clusters are labeled as “*weed*” while the rest of the image is annotated as “*background*”. The splitting process was repeated 3 times aiming to create subsets with different class distribution in order to conduct a more thorough evaluation of the employed detector. Also:
* The model was trained for *500 epochs* with a *batch size of 12*. 
* As an optimization algorithm, *Adam solver* with a *learning rate equal to 10−3* was selected.
* In order to tackle the imbalance issue among the dataset classes, *focal loss* was employed. 
* *Data augmentation techniques* were utilized to enhance the generalization ability of the model. In specific, every input image of the training set was horizontally/vertical flipped and randomly resized in a scale between 0.5 to 1.5 times of the initial size with a chance of 50%. 
  
In Table 1, we present the results of the detector per split and in Figure 1 an overview of the Weeds-Detection module.
  
<div align="center">
  
|      |Background|Weed| mIoU
| :---:  | :---: | :---: | :---: | 
Split 1|95.44|44.93|70.18
Split 2|95.83|43.49|69.66
Split 3|96.62|43.96|70.29
<figcaption align = "center"><p align="center">Table 1. Model accuracy in terms of IoU (%).</figcaption>
</figure>
</div>


<p align="center">
<img src="https://user-images.githubusercontent.com/80779522/149305858-3b9a42d4-9e88-4351-a160-c6a61ff8fe55.png"/>
<figcaption align = "center"><p align="center">
  Figure 1. Workflow of the Weed-Detection module. The detected weeds are annotated with pink color.
    </figcaption>
  
  
## How to run
  
1. Clone this repo
2. Open terminal on ~REPO_PATH
3. Run:
```
python3 weed_detection.py --input_folder ~INPUT_FOLDER_PATH --output_folder ~OUTPUT_FOLDER_PATH
```
**ARGUMEΝTS**
  * ```--input_folder```:  refers to the path of the folder where the images are stored
  * ```--output_folder```: refers to the path where the annotated images and the corresponding masks will be saved

## Results
  
### Visualizations  
  <table class="center">
   <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/148941318-6922edc4-a11e-47f7-8feb-71659367fe80.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149325086-f561b75f-51f2-4624-88fb-6649e9a740ac.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202187-d4f62556-a42a-4bf3-a601-826848c9b23c.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201959-c48a2f4f-c074-4b09-a286-2d6dbf4a9276.png" align="center" /></td> 
   </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201791-2628f904-27fb-4a46-8bc4-6e88a4ad7e95.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324542-0752b92b-b1e8-4459-b656-0771a21b4753.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202191-0fccd089-e610-4271-9154-55444fe58279.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202065-e13630bb-2a8e-4aaf-8832-2da1f079407e.png" align="center" /></td> 
   </tr> 
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202267-3c24a3dd-97d3-439b-b647-142bd64278a8.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324545-a39c8edd-3c8b-4298-9c8b-b17278270c7a.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202190-9fb88165-98e1-45e8-90f6-77e5c1ba55dd.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202002-d49ab489-83a5-4ea7-98f0-90c9c7e7835b.png" align="center" /></td> 
   </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201857-eeb19a19-14e9-4dae-b3c6-0ed8886677a3.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324548-6b5a1ef2-cfd7-488b-8292-fd372453f015.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202195-9c0614c3-606d-402e-a84b-d389dbf35619.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202098-b8eda456-4f4a-4ffa-ad88-8412dc38d47a.png" align="center" /></td> 
   </tr>
   <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201901-e90286db-6277-4220-b236-0587ff1ac385.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324538-eb4238c9-f20e-45ab-a843-5295e13de105.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202196-e54ae7a6-cc51-46f7-bc3e-7b38511b4dc3.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202140-b268fc66-b533-4a92-a9d2-380baface177.png" align="center" /></td> 
   </tr> 
 
   <tr align="center">
    <td>(a) Input RGB image</td>
    <td>(b) Ground truth</td>
    <td>(c) Predicted mask</td>   
    <td>(d) Overlay</td>
  </tr>  
 </table>
 
  <figcaption align = "center"><p align="center">
  Figure 2. Results from the Weed-Detection module.
<!--   with (a) RGB images as inputs (b) the ground truths and the corresponding (c) predicted masks and (d) overlays as extracted.   The ground truths have been extracted by agronomists, as mentioned in  CoFly-WeeDB repository. -->
    </figcaption>

## Dependencies 
Install all the neccecary dependencies using ```pip3 install <package name>```

Required packages:
* argparse (version >= 1.1)
* opencv-python (version >= 4.5.3)
* numpy (version >= 1.19.5)
* matplotlib (version >= 3.2.2)
* tensorflow (version >= 2.7.0)
* keras (version == 2.7.0)
* [segmentation-models](https://github.com/qubvel/segmentation_models) (version == 1.0.1)

> Note: The versions of tensorflow, keras and segmentation-models should be compatible. 

## Citation
(not published yet)

## Acknowledgment
This research has been financed by the European Regional Development Fund of the European Union and Greek national funds through the Operational Program Competitiveness, Entrepreneurship and Innovation, under the call RESEARCH - CREATE - INNOVATE (T1EDK-00636).
