import os


def audio_to_flac(audio_in_path, audio_out_path, sample_rate=48000, no_log=True):
    log_cmd = ' -v quiet' if no_log else ''
    os.system(
        f'ffmpeg -y -i "{audio_in_path}" -vn {log_cmd} -flags +bitexact '
        f'-ar {sample_rate} -ac 1 "{audio_out_path}"')


def audio_to_mp3(audio_in_path, audio_out_path, bit_rate='192k', no_log=True):
    log_cmd = ' -v quiet' if no_log else ''
    os.system(
        f'ffmpeg -y -i "{audio_in_path}" -vn {log_cmd}  '
        f'-b:a {bit_rate} -ac 1 "{audio_out_path}"')
