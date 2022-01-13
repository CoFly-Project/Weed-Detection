<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

# Weed-Detection
  
The main objective of the ```Weed-Detection``` module is to provide a more thorough inspection on problematic areas, as have been extracted from the [```Problematic-Areas-Detection```](https://github.com/CoFly-Project/Problematic-Areas-Detection) module in terms of plant health and provide valuable information to the end-user. In specific, the developed module is based on the pretrained [DeepLabv3+](https://github.com/qubvel/segmentation_models) instance was pretrained on PASCAL VOC 2012 dataset and further trained on the  [```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB) dataset for the weed semantic segmentation task. The developed module is capable of semantically segmenting weed instances depicted on input RGB images and thus, provides accurate information regarding the location of detected weeds. In Figure 1 an overview of the Weeds-Detection module.
  
<p align="center">
<img src="https://user-images.githubusercontent.com/80779522/149305858-3b9a42d4-9e88-4351-a160-c6a61ff8fe55.png"/>
<figcaption align = "center"><p align="center">
  Figure 1. Workflow of the Weed-Detection module. The detected weeds are annotated with pink color.
    </figcaption>
  
Concerning about the training and evaluation of the detector, the developed dataset ([```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB)) was split to a training (80%) and a testing (20%) set where depicted weed clusters are labeled as “*weed*” while the rest of the image is annotated as “*background*”. The splitting process was repeated 3 times aiming to create subsets with different class distribution in order to conduct a more thorough evaluation of the employed detector. Also:
* The model was trained for *500 epochs* with a *batch size of 12*
* As an optimization algorithm, *Adam solver* with a *learning rate equal to 10−3* was selected
* In order to tackle the imbalance issue among the dataset classes, *focal loss* was employed
* *Data augmentation techniques* were utilized to enhance the generalization ability of the model. In specific, every input image of the training set was horizontally/vertical flipped and randomly resized in a scale between 0.5 to 1.5 times of the initial size with a chance of 50%
  
In Table 1, we present the results of the detector per split and 
  
<div align="center">
  
|      |Background|Weed| mIoU
| :---:  | :---: | :---: | :---: | 
Split 1|95.44|44.93|70.18
Split 2|95.83|43.49|69.66
Split 3|96.62|43.96|70.29
<figcaption align = "center"><p align="center">Table 1. Model accuracy in terms of IoU (%).</figcaption>
</figure>
</div>

<!-- ![ID_00048_UAV_dji phantom 4 pro hawk 1_ Lat=39 54212427861807,Lon=22 64442951302024,Alt=4 900000095367432 _DATE_03_07_2019_14_38_56](https://user-images.githubusercontent.com/80779522/149367634-127c1619-c594-4dc6-9746-4cb5d45a68fb.png)
![ID_00049_UAV_dji phantom 4 pro hawk 1_ Lat=39 54212238368247,Lon=22 644427100249906,Alt=4 900000095367432 _DATE_03_07_2019_14_38_57](https://user-images.githubusercontent.com/80779522/149367641-98c69eea-c961-4133-b668-41d4c097cbea.png)
![ID_00052_UAV_dji phantom 4 pro hawk 1_ Lat=39 54211477371615,Lon=22 644417506003943,Alt=4 900000095367432 _DATE_03_07_2019_14_38_59](https://user-images.githubusercontent.com/80779522/149367645-ad9045b1-db9d-42ed-8c7d-0b492ca084f4.png)
![ID_00053_UAV_dji phantom 4 pro hawk 1_ Lat=39 542112844908914,Lon=22 64441509154499,Alt=4 900000095367432 _DATE_03_07_2019_14_39_00](https://user-images.githubusercontent.com/80779522/149367648-28d000f3-c047-4eeb-ba65-ea317601bf64.png)
![ID_00056_UAV_dji phantom 4 pro hawk 1_ Lat=39 54203384270712,Lon=22 6443173135562,Alt=4 900000095367432 _DATE_03_07_2019_14_39_01](https://user-images.githubusercontent.com/80779522/149367650-fef3be86-04e5-468b-bed2-f6f153f5917c.png)
![ID_00057_UAV_dji phantom 4 pro hawk 1_ Lat=39 542029925582796,Lon=22 644312197750764,Alt=4 900000095367432 _DATE_03_07_2019_14_39_02](https://user-images.githubusercontent.com/80779522/149367653-88f1d43d-612b-4bc6-9b3f-edd7ac3fd964.png)
![ID_00058_UAV_dji phantom 4 pro hawk 1_ Lat=39 54202799708822,Lon=22 644309643225288,Alt=4 900000095367432 _DATE_03_07_2019_14_39_04](https://user-images.githubusercontent.com/80779522/149367656-4ac2613e-886f-4e26-94b0-c97dacce08a8.png)
![ID_00061_UAV_dji phantom 4 pro hawk 1_ Lat=39 54190261857315,Lon=22 64415333458149,Alt=5 0 _DATE_03_07_2019_14_39_11](https://user-images.githubusercontent.com/80779522/149367661-113c38f2-5077-4c78-b68f-e03d6ac33a0d.png)
![ID_00068_UAV_dji phantom 4 pro hawk 1_ Lat=39 541760147284556,Lon=22 643725690503484,Alt=4 900000095367432 _DATE_03_07_2019_14_39_28](https://user-images.githubusercontent.com/80779522/149367672-8da26015-0414-4430-8c43-d9b8b793193e.png)
![ID_00074_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193593867384,Lon=22 643553973830834,Alt=4 900000095367432 _DATE_03_07_2019_14_39_31](https://user-images.githubusercontent.com/80779522/149367696-b949e1d0-77a2-43e4-995a-aafafb3b3bd9.png)
![ID_00082_UAV_dji phantom 4 pro hawk 1_ Lat=39 541931324836035,Lon=22 644130139884748,Alt=4 900000095367432 _DATE_03_07_2019_14_39_50](https://user-images.githubusercontent.com/80779522/149367714-a3abebef-11ea-4091-a004-4bb3205f673c.png)
![ID_00083_UAV_dji phantom 4 pro hawk 1_ Lat=39 541931332861004,Lon=22 644133585734583,Alt=4 900000095367432 _DATE_03_07_2019_14_39_52](https://user-images.githubusercontent.com/80779522/149367750-b149fed8-9322-44cd-a8bc-e2f15a2d53d1.png)
![ID_00086_UAV_dji phantom 4 pro hawk 1_ Lat=39 541931373298524,Lon=22 644143932704814,Alt=4 900000095367432 _DATE_03_07_2019_14_39_58](https://user-images.githubusercontent.com/80779522/149367779-b0e4fe8e-97c3-44bb-9542-84f494515aa4.png)
![ID_00088_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193316161664,Lon=22 644220651922506,Alt=4 800000190734863 _DATE_03_07_2019_14_39_59](https://user-images.githubusercontent.com/80779522/149367808-4a3fea08-3c6c-458a-8168-9640b02bf147.png)
![ID_00091_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193035860856,Lon=22 644614169849085,Alt=4 900000095367432 _DATE_03_07_2019_14_40_00](https://user-images.githubusercontent.com/80779522/149367845-f1e8a6fa-2fbd-453f-8215-f5a6a2008b6d.png)
![ID_00096_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193248783165,Lon=22 644830630289068,Alt=4 900000095367432 _DATE_03_07_2019_14_40_10](https://user-images.githubusercontent.com/80779522/149367875-9e8703cc-9372-4611-a09c-db265a5c11b5.png)
![ID_00097_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193245666975,Lon=22 644834155659538,Alt=5 0 _DATE_03_07_2019_14_40_11](https://user-images.githubusercontent.com/80779522/149367916-d84e7154-4f8f-4d2d-a9e3-be135ab52c33.png)
![ID_00106_UAV_dji phantom 4 pro hawk 1_ Lat=39 541931716392135,Lon=22 645561071289258,Alt=4 900000095367432 _DATE_03_07_2019_14_40_29](https://user-images.githubusercontent.com/80779522/149367950-c665c92e-c255-4613-b872-7ce0e6ffafcb.png)
![ID_00110_UAV_dji phantom 4 pro hawk 1_ Lat=39 541930847402305,Lon=22 645747946119535,Alt=5 0 _DATE_03_07_2019_14_40_32](https://user-images.githubusercontent.com/80779522/149367976-d4cb0c4b-200a-4b74-969d-6a0b359ef1bd.png)
![ID_00111_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193005334696,Lon=22 645817738398737,Alt=5 0 _DATE_03_07_2019_14_40_36](https://user-images.githubusercontent.com/80779522/149368013-bafb6c52-40a5-449f-b927-6a7690989736.png)
![ID_00115_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193493669876,Lon=22 64617081087172,Alt=4 900000095367432 _DATE_03_07_2019_14_40_48](https://user-images.githubusercontent.com/80779522/149368041-3006c53c-d079-4a52-9ace-f9cd8a2fe869.png)
![ID_00116_UAV_dji phantom 4 pro hawk 1_ Lat=39 54193509084076,Lon=22 64617422028293,Alt=4 900000095367432 _DATE_03_07_2019_14_40_50](https://user-images.githubusercontent.com/80779522/149368060-254f77f0-d1be-49b6-9a9a-11d1f9932982.png)
![ID_00120_UAV_dji phantom 4 pro hawk 1_ Lat=39 54210226914222,Lon=22 646142643191187,Alt=5 0 _DATE_03_07_2019_14_40_58](https://user-images.githubusercontent.com/80779522/149368077-96aa3ba2-888a-4089-9691-3cbac1a7d998.png)
![ID_00129_UAV_dji phantom 4 pro hawk 1_ Lat=39 542102571277205,Lon=22 645483517538135,Alt=5 0 _DATE_03_07_2019_14_41_15](https://user-images.githubusercontent.com/80779522/149368112-1f54a46f-2614-4c88-8900-bf154c84db88.png)
![ID_00135_UAV_dji phantom 4 pro hawk 1_ Lat=39 5421032925867,Lon=22 64506277085889,Alt=5 0 _DATE_03_07_2019_14_41_27](https://user-images.githubusercontent.com/80779522/149368139-40c11601-1420-4d24-98ac-7ff103852e70.png)
![ID_00136_UAV_dji phantom 4 pro hawk 1_ Lat=39 54210393948282,Lon=22 644992056004764,Alt=5 0 _DATE_03_07_2019_14_41_27](https://user-images.githubusercontent.com/80779522/149368176-fcb4ab0a-8a7b-4f3d-b52d-de3763908763.png)
![ID_00138_UAV_dji phantom 4 pro hawk 1_ Lat=39 54210701481885,Lon=22 644849797228876,Alt=5 0 _DATE_03_07_2019_14_41_31](https://user-images.githubusercontent.com/80779522/149368210-7b6b3daa-954d-4307-97f8-1e8e8d4a6efa.png)
![ID_00142_UAV_dji phantom 4 pro hawk 1_ Lat=39 54210676625316,Lon=22 644570296231713,Alt=5 0 _DATE_03_07_2019_14_41_43](https://user-images.githubusercontent.com/80779522/149368238-7ed2ac39-c1ce-4e3a-8980-5c29ed0f1ca4.png)
![ID_00145_UAV_dji phantom 4 pro hawk 1_ Lat=39 54218646912881,Lon=22 644424401747415,Alt=5 0 _DATE_03_07_2019_14_41_49](https://user-images.githubusercontent.com/80779522/149368278-fb0590d0-4913-40dc-b0c9-7e0d79f82b7b.png)
![ID_00147_UAV_dji phantom 4 pro hawk 1_ Lat=39 54226945067451,Lon=22 64442726480141,Alt=5 0 _DATE_03_07_2019_14_41_54](https://user-images.githubusercontent.com/80779522/149368289-9e1e1e21-b680-4e63-8bff-c2c371e8c8ec.png)
![ID_00150_UAV_dji phantom 4 pro hawk 1_ Lat=39 54227810300132,Lon=22 644643009866716,Alt=4 900000095367432 _DATE_03_07_2019_14_41_58](https://user-images.githubusercontent.com/80779522/149368291-a1fe6d41-e6ad-48ab-a083-0e4648fb5aa4.png)
![ID_00151_UAV_dji phantom 4 pro hawk 1_ Lat=39 542278121761,Lon=22 644646552367792,Alt=4 900000095367432 _DATE_03_07_2019_14_41_58](https://user-images.githubusercontent.com/80779522/149368293-7b9f8afe-82aa-462c-81b5-2f383538095a.png)
![ID_00162_UAV_dji phantom 4 pro hawk 1_ Lat=39 5422813419113,Lon=22 645436838479792,Alt=5 0 _DATE_03_07_2019_14_42_23](https://user-images.githubusercontent.com/80779522/149368296-4a0a437e-63c4-4945-8d4f-a314b07e2ab8.png)
![ID_00168_UAV_dji phantom 4 pro hawk 1_ Lat=39 54230450578458,Lon=22 645749401931546,Alt=5 099999904632568 _DATE_03_07_2019_14_42_32](https://user-images.githubusercontent.com/80779522/149368297-a4d0fe75-e8ac-4c8d-ad56-9853cbc0269a.png)
![ID_00170_UAV_dji phantom 4 pro hawk 1_ Lat=39 54241457364314,Lon=22 645743751011544,Alt=5 0 _DATE_03_07_2019_14_42_37](https://user-images.githubusercontent.com/80779522/149368302-fdefcd7f-7690-4a86-a7e0-ee3af469f4cb.png)
![ID_00174_UAV_dji phantom 4 pro hawk 1_ Lat=39 54244811839094,Lon=22 64553941692437,Alt=4 900000095367432 _DATE_03_07_2019_14_42_46](https://user-images.githubusercontent.com/80779522/149368303-0106030a-8c85-4173-9606-529e23b2b159.png)
![ID_00177_UAV_dji phantom 4 pro hawk 1_ Lat=39 54244840442387,Lon=22 645332618430654,Alt=4 900000095367432 _DATE_03_07_2019_14_42_54](https://user-images.githubusercontent.com/80779522/149368308-f4f2166c-1cf5-4271-9952-a4f8fe806ba2.png)
![ID_00183_UAV_dji phantom 4 pro hawk 1_ Lat=39 542451006911875,Lon=22 644911984033477,Alt=4 900000095367432 _DATE_03_07_2019_14_43_02](https://user-images.githubusercontent.com/80779522/149368312-ff83edc1-65ac-495d-b496-654758173240.png)
![ID_00187_UAV_dji phantom 4 pro hawk 1_ Lat=39 54261113579653,Lon=22 64486757250199,Alt=5 0 _DATE_03_07_2019_14_43_12](https://user-images.githubusercontent.com/80779522/149368319-b924ee6c-0187-40f7-8edb-ec3ab197a32c.png) -->



<table class="center">
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149367627-2c1f4e1b-3eeb-4a38-89db-a786460b1a95.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368361-3558e68c-b6ad-4b8f-8b2e-be15965b24c3.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368347-32a105db-569f-4a05-b2a6-8cf92225349f.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368342-7ca5a199-380e-4f8d-853e-f6e2bfeba267.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368337-9877ccb8-cd25-4104-83c4-b85750c90ad2.png" align="center" /></td> 
      </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368332-57330c45-a921-44a9-a236-9564b7a73349.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368329-515ae162-facd-4c30-8680-9f7eb3400fa5.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368327-c2ba3487-dd3b-4ed3-8b8e-ce531b6cc07e.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368323-0787ee02-3d97-4e44-80af-3925967cbef7.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368507-78f41e77-83bc-432b-8669-fee734d4fca2.png" align="center" /></td>
       </tr>
  <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368503-fc735baf-a0cb-44d2-bfaa-c2611c3a4ad9.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368501-9785bad9-26e8-4da5-8c28-e44889b7bda7.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368496-0781dc80-90a2-46f4-ad95-8112e06c09a3.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368485-3df0c3eb-851f-4efd-b4eb-453329862ac7.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368453-f9592cf2-6e2b-4723-ae34-36f348bf76dd.png" align="center" /></td>
     </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368421-702f6094-fd7c-4074-a536-50ad98bcbd5a.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368395-547bcb21-25fa-4eec-b567-0216619a6eb6.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368681-af7005df-53c3-427c-a9fa-09340593e28f.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368645-0e7e1f9b-dc80-4a8e-9375-c79cd0d8d57a.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368615-27853822-deae-4954-a23d-b781c4559c17.png" align="center" /></td>  
       </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368586-54aadd7f-829a-4e43-a026-eb3d347fe332.png" align="center" /></td> 
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368553-ce120276-1a30-486d-8d12-f1f337e72041.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368519-ff0c6b1a-c18f-4a09-bb8a-ba24cb256f53.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368512-ba101685-6e8d-4ff1-b22c-2d2f77661aa0.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149368511-9d099def-cece-4b65-8acd-9784e52b33e9.png" align="center" /></td> 
   </tr>
   </table>
<figcaption align = "center"><p align="center">
  Figure 2. Samples images of testing set.
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
