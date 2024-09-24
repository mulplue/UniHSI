python3 unihsi/run.py --wandb_name hard_16 \
    --task UniHSI_PartNet_Train\
    --cfg_env unihsi/data/cfg/humanoid_unified_interaction_scene_16.yaml \
    --cfg_train unihsi/data/cfg/train/rlg/amp_humanoid_task_deep_layer_4we.yaml \
    --motion_file motion_clips/training.yaml \
    --output_path output/ \
    --obj_file sceneplan/partnet_train_hard.json \
    --headless \
    --resume 1 \
    --checkpoint /home/jiahe/3_motion_generation/UniHSI/output/Humanoid_24-10-34-06/nn/Humanoid30000.pth # checkpoint trained by mid