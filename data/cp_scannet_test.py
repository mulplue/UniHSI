import shutil
import os

obj_list = ["scene0000_00", "scene0004_00", "scene0006_00", "scene0008_00",
            "scene0009_00", "scene0010_00", "scene0013_00", "scene0015_00", 
            "scene0025_00", "scene0030_00"]
            
            

def copy_file(source_path, destination_path):
    
    shutil.copy(source_path, destination_path)
    print(f"File copied successfully from {source_path} to {destination_path}")


for obj_id in obj_list:
    source_file =  "scannet_origin/scans/"+obj_id+"/"+obj_id+"_vh_clean_2.ply"
    target_file = "scannet/"+obj_id+"_vh_clean_2.ply"
    copy_file(source_file, target_file)

    source_file =  "scannet_origin/scans/"+obj_id+"/"+obj_id+"_vh_clean.aggregation.json"
    target_file = "scannet/"+obj_id+"_vh_clean.aggregation.json"
    copy_file(source_file, target_file)

    # source_file =  "scannet_origin/scans/"+obj_id+"/"+obj_id+"_vh_clean_2.0.010000.segs"
    # target_file = "scannet/"+obj_id+"_vh_clean_2.0.010000.segs"
    source_file =  "scannet_origin/scans/"+obj_id+"/"+obj_id+"_vh_clean_2.0.010000.segs.json"
    target_file = "scannet/"+obj_id+"_vh_clean_2.0.010000.segs.json"
    copy_file(source_file, target_file)
