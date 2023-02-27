from pyChatGPT import ChatGPT
from pprint import pprint
import whisper
import gradio as gr
import time
import warnings
import torch


warnings.filterwarnings("ignore")


session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Hgqae-zcRNu8Qg8W.PW6vjGOj3cpic-_LoTzEvxoEdVVxPqVhL9LlWZtFGUf4dRxNIAyUgEoVY88-MBYgyKZj91bPrfG0_mz1tOshA1mRFD4EHEk_79ZQWMlBAmWUsl72V3FovIvJQ0U6QK5kDcNmjxUfj_Om_HOYGrXdIKm0OoM6OzZQ4L0_gaE4eqbplT36lduDuWHLLclHz_sEb2yOkZ8vCI_D7_IK2CQ-S8w7j5YB5_X0s9G-w-4ReQGnkj6g20ahwhIqGWJ1mzxbLwiLskcc1RRwxBLAgpNRNU_P4ju6ZE6YcCSI0VuophYaUYuwaqdag-UdFpmY80f7-PLOjps92iUki4jQrL4ctqWFlADeOj_eDRnoO06WZRXEp4jDF0fGA6fztzyW9y4lhpkcHz16z12GxTnLFK3Yy8eR8Wrk_rVX6r2MdbLUrjYflM2EOOfdJH9O3oiPxCc69351ZskAZYvQrbS-qvy2ewAqcGl-q-ROgLPLXNptvewzkmonjArkGKrI2uKiKUsoVL0C1c2NcdlG2luQ2-VhoXpmDXMJWA1aqpRDKyrpM4zh_P7NOBQHy0kY0GCAbNwVgZeIylpjfV6UyDfCOh-dNAzVBzaSbifKA-VEWSZQkTwtnd_DCKKmmPlaHbWXgfjXfdR-kj3MKUn4kFG5qOIkeNS384r8JoexvgSDQpBFVoUxU_YRpgBSn9z5ptio52YvdFIyC8uOPKDSDvSK49AoL02scdPMjYNVw3fQeb9Ts3GazUu9MxKg5II6Nv_HsHp5u4Uw0xHlDvtEc5SNHKETXn0a2JXV1cj0_LYMC5m9Wa7GdsI3-wK96u-0M5lKnztsZi7SNKN0rWBlGWr6AY3KkbWt-QzyHZUEVqSAELjQ--ui-_dzef5-h3VZ5fCX-6PFfEXzwUu1K_NEId8uxQAOK2U2zCnSIKOthmnMjxno5yPbrMQi4oRFgUATsue3bQ9IBdhTYGBVhxYEAJkwK166dV4jPpe2e58O9g28yGdZfwHSyU2FsZ5y5R1RcT9B_6Noy8_wI0ihrei5BH57_rl52bNJ5Q9g8G_dYQlDKVS5rF0KCqdOm_5w-dkH0Sx8tA4Rr6vhx-M93wlv50Wf4S4hj9O7mwEiMSB19oQcLEXzhAcNJ6-qqegSXEv1Y0OX-kFakr35z9zAxyUEK9BoLm8k-jyds81FKhn6UtF075jDkIU6IJ16XbNV--hAKfJZ3LYK0Dg7D49rknJsPxftFFCoVc3J7rojaTVjaBZaAquO1uoZmYQO6DFsLM9WwE_xnSYYBd-_plnuWASLhDf_kFE6we2UancS2QKZH1F8TIwQrAbBktFrAuLkA1PLM0ygBDeR7H_kLowd6Ph_PGQZgaE4APzjSglyjRCTQ29twEy7YMu7Mi_zL-HZUzCDiWkFEGwlPNvJvbPGRP-n9OpsUYXPH5f3StbwCQyDprx2BagrXN5Bk6ROnJE9LIOmt4iOefn2Lo0Nl2bKfDmKpLDrOAHGzk72HNZHmShUmW565ecL2MWVzy2in4uo2AC6kvh3Fysiy5M3AEuTrGs2o6tqwNunhQeSUm6nq1wkkYA6TIx1SrmAx002wgRnIdZcyrOt2ZH7Hs7q2ZmiiNcHhP06eqkM7TFPScUsJw1pEJVFkSXRVX3F_ScYN48cD9_Kenm9pQnexS1inMiM2IOS9mFkwTsVNhuFZankCzz5p2Mcmgz9-itLVudDQ2QPQ_0AkPRhy5hZ5dDXn_7ev5fUPZBUubcICuse3fflagFZygyE4LM98A1aw_wQVbQ8RrIYrlXHUVHMimE8wWf3d6Mi4hxrRTo5x94cyfm8rh8VWCTITCd71eo2nbkS-Q-_Eu-ZwHPdb7IDNREsjLkROAoztY2iVTMrSyjcKMb_QrPKKzCYXlvMEzck-XnCLrEdeH4pga6SFyFWfEZOaav0XGCdNqISaVSdp5tUIg2VpbXUbDOHtRwzC4wSsoEq34r3tm2v-V69CRt8dPCEwnk-kftsi7L0HPkSar5piZ4P2xlWSOKpn99n9nyblpQb_8Z6UdET8WGmYvRoJcWjEWM7mcUoWVHhXqrTmOYE4X09_KccLtNaKSQhow-wEr3OujUvmgjj8MqKWxf4aCCmIfIH-7buU_D15L1aZpWXMVvtMhIxdugRA_BPOk0qdpL3yYWGF0JJVEGXzlktW4iEym5JugE2qBHDQSlnVjPRtC-hgKt3zAk-GU-9wwajg-6qoTs9qH1IpALslGvptQznazGW-6hBPr1xWMrJO8Jp1kkjx2IQc42aI5PVh79jy7RojU2GjXA.OpkQ04QnK33bS1sKk6dIjQ"
model = whisper.load_model("base")

device= torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def transcribe(audio):
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio= audio).to(device)

    # detect the spoken language
    _, probs = model.detect_language(mel= mel)

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    result_text = result.text

    # pass the generated text to Audio
    ChatGPT_api = ChatGPT(session_token)
    resp = ChatGPT_api.send_message(result_text)
    out_result = resp['message']

    return [result_text, out_result]

    
output_1 = gr.Textbox(label= 'Seech to Text')
output_2 = gr.Textbox(label='ChatGPT Output')

gr.Interface(
    title= 'OpenAI Wisper and chatGPT ASR Gradio Web UI',
    fn = transcribe,
    inputs=[
    gr.input.Audio(source= 'microphone', type = 'filepath')
    ],
    outputs=[
    output_1, output_2
    ],
    live=True).launch()

