python3 unihsi/run.py --wandb_name mid_16 \
    --task UniHSI_PartNet_Train\
    --cfg_env unihsi/data/cfg/humanoid_unified_interaction_scene_16.yaml \
    --cfg_train unihsi/data/cfg/train/rlg/amp_humanoid_task_deep_layer_3we.yaml \
    --motion_file motion_clips/training.yaml \
    --output_path output/ \
    --obj_file sceneplan/partnet_train_mid.json \
    --headless \
    --resume 1 \
    --checkpoint output/Humanoid_23-19-45-51/nn/Humanoid20000.pth # checkpoint trained by simple