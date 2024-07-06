#!/bin/bash

# Define the dimension list
dimensions=("subject_consistency" "background_consistency" "aesthetic_quality" "imaging_quality" "object_class" "multiple_objects" "color" "spatial_relationship" "scene" "temporal_style" "overall_consistency" "human_action" "temporal_flickering" "motion_smoothness" "dynamic_degree" "appearance_style")

for checkpoint_dir in $(ls -d data/inference_result/*); do
    # Loop over each dimension
    for i in "${!dimensions[@]}"; do
        # Get the dimension and corresponding folder
        dimension=${dimensions[i]}
        folder=${folders[i]}

        dir=$(basename $checkpoint_dir)

        videos_path="./data/inference_result/${dir}"

        output_path="./evaluation_results/${dir}"
        echo "$dimension $videos_path $output_path"

        # Run the evaluation script
        python run_eval.py --videos_path $videos_path --dimension $dimension --output_path $output_path --mode=custom_input
    done
done