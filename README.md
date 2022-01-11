<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

# Weed-Detection
  
The main objective of the ```Weed-Detection``` module is to provide a more thorough inspection on problematic areas, as have been extracted from the [```Problematic-Areas-Detection```](https://github.com/CoFly-Project/Problematic-Areas-Detection) module in terms of plant health and provide valuable information to the end-user. In specific, the developed module is based on the pretrained DeepLabv3+ instance and further trained on the  [```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB) dataset for the weed semantic segmentation task. The developed module is capable of semantically segmenting weed instances depicted on input RGB images and thus, provides accurate information regarding the location of detected weeds.
  
  
## How to run
  
1. Clone this repo
2. Open terminal on ~REPO_PATH
3. Run:
```
python3 weed_detection.py --input_folder ~INPUT_FOLDER_PATH --output_folder ~OUTPUT_FOLDER_PATH
```
**ARGUMEΝTS**
  * ```--input_folder```:  refers to the path of the folder where the images are stored
  * ```--output_folder```: refers to the path where extracted annotated images will be saved
  

## Results

### Visualizations
  
<!-- ![ID_00048_UAV_dji phantom 4 pro hawk 1_ Lat=39 54212427861807,Lon=22 64442951302024,Alt=4 900000095367432 _DATE_03_07_2019_14_38_56](https://user-images.githubusercontent.com/80779522/148941318-6922edc4-a11e-47f7-8feb-71659367fe80.png)
![ID_00050_UAV_dji phantom 4 pro hawk 1_ Lat=39 54212050531792,Lon=22 644424707209755,Alt=4 900000095367432 _DATE_03_07_2019_14_38_58](https://user-images.githubusercontent.com/80779522/148941380-d254c284-62ba-412a-9823-e0d96b3713fc.png)
![ID_00052_UAV_dji phantom 4 pro hawk 1_ Lat=39 54211477371615,Lon=22 644417506003943,Alt=4 900000095367432 _DATE_03_07_2019_14_38_59](https://user-images.githubusercontent.com/80779522/148941430-b8d319fc-66ea-43ee-97be-d1c2bd6b6685.png) -->
  
  
Examples of the CoFly-WeedDB dataset.
<table class="center">
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80779522/148941318-6922edc4-a11e-47f7-8feb-71659367fe80.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80779522/148940518-fe3bd215-745f-45cf-883e-c7d1bb921cf6.png" =500x500 /></td>
    </tr>
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80779522/148941430-b8d319fc-66ea-43ee-97be-d1c2bd6b6685.png" =500x500/></td>  
    <td><img src="https://user-images.githubusercontent.com/80779522/148940616-39bb486e-5b42-4ba6-8c24-e8d383b0ec26.png" =500x500 /></td>
     </tr>
  <tr align="center">
    <td>(a) RGB</td>
    <td>(b) Overlay</td>
  </tr>
</table>
     <figcaption align = "center"><p align="center">
  Figure 1. Detected weeds annotated with pink color.
    </figcaption>
