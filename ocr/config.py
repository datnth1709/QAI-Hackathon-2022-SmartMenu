import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_ROOT = BASE_DIR
print(BASE_DIR + "/data/")
INPUT_ROOT =  BASE_DIR + "/data/"
OUTPUT_ROOT = BASE_DIR + "/output/"


def full_path(sub_path, file=False):
    path = os.path.join(CONFIG_ROOT, sub_path)
    if not file and not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print('full_path. Error makedirs',path)
    return path


def output_path(sub_path):
    path = os.path.join(OUTPUT_ROOT, sub_path)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print('output_path. Error makedirs',path)
    return path

gpu = "0" # None or "0","1","2"...
# dataset = 'train/ocr/image'
dataset = 'SmartMenu/image'
# mc_ocr_train_filtered
# mc_ocr_private_test
# wer_20210125
# viReceipts

# input data from organizer
# raw_train_img_dir = full_path('data/mc_ocr_train')
raw_img_dir=full_path('data/{}'.format(dataset))
# raw_csv = full_path('data/mcocr_train_df.csv', file=True)

# EDA
# json_data_path = full_path('EDA/final_data.json', file=True)
# filtered_train_img_dir=full_path('data/mc_ocr_train_filtered')
# filtered_csv = full_path('data/mcocr_train_df_filtered.csv', file=True)

#splitor
crop_dir = output_path('{}/'.format("croped"))

# text detector
det_model_dir = full_path('ocr/text_detector/models/ch_ppocr_server_v2.0_det_infer')
det_visualize = True
det_db_thresh = 0.3
det_db_box_thresh = 0.3
det_out_viz_dir = output_path('{}/'.format(dataset))
det_out_txt_dir = output_path(f'{dataset}/'.replace('image', 'label'))

# rotation corrector
# rot_drop_thresh = [.5, 2]
# rot_visualize = True
# rot_model_path = full_path('rotation_corrector/weights/mobilenetv3-Epoch-487-Loss-0.03-Acc-0.99.pth', file=True)
# rot_out_img_dir = output_path('rotation_corrector/{}/imgs'.format(dataset))
# rot_out_txt_dir = output_path('rotation_corrector/{}/txt'.format(dataset))
# rot_out_viz_dir = output_path('rotation_corrector/{}/viz_imgs'.format(dataset))
# rotate_filtered_csv = full_path('data/mcocr_train_df_rotate_filtered.csv', file=True)

# text classifier (OCR)
# cls_visualize = True
# cls_ocr_thres = 0.65
# cls_model_path = full_path('text_classifier/vietocr/vietocr/weights/vgg19_bn_seq2seq.pth', file=True)
# cls_base_config_path = full_path('text_classifier/vietocr/config/base.yml', file=True)
# cls_config_path = full_path('text_classifier/vietocr/config/vgg-seq2seq.yml', file=True)
# cls_out_viz_dir = output_path('text_classifier/{}/viz_imgs'.format(dataset))
# cls_out_txt_dir = output_path('text_classifier/{}/txt'.format(dataset))

# key information
# kie_visualize = True
# kie_model = full_path('key_info_extraction/PICK/saved/models/PICK_Default/test_0121_212713/model_best.pth', file=True)
# kie_boxes_transcripts = output_path('key_info_extraction/{}/boxes_and_transcripts'.format(dataset))
# kie_out_txt_dir = output_path('key_info_extraction/{}/txt'.format(dataset))
# kie_out_viz_dir = output_path('key_info_extraction/{}/viz_imgs'.format(dataset))

# submision
# best_task1_csv = full_path('submit/{}/best_task1_0.11609/results.csv'.format(dataset), file=True)
# submit_sample_file = full_path('submit/{}/mcocr_test_samples_df.csv'.format(dataset), file=True)
# output_submission_file = full_path('submit/{}/results.csv'.format(dataset), file=True)
