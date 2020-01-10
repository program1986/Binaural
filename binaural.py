import wave, struct, math
import scipy.signal as signal

reference_table = \
    {
        'l5': 391.995436,
        'l5.5': 415.3046976,
        'l6': 440,
        'l6.5': 466.1637615,
        'l7': 493.8833013,
        'm1': 523.2511306,
        'm1.5': 554.365262,
        'm2': 587.3295358,
        'm2.5': 622.2539674,
        'm3': 659.2551138,
        'm4': 698.4564629,
        'm4.5': 739.9888454,
        'm5': 783.990872,
        'm5.5': 830.6093952,
        'm6': 880,
        'm6.5': 932.327523,
        'm7': 987.7666025

    }


def open_wave_file(sample_rate, filename):
    # duration = 1.0  # seconds
    # Use different frequencies for the left and right channels
    wave_file = wave.open(filename, 'w')
    wave_file.setnchannels(2)  # stereo
    wave_file.setsampwidth(2)
    wave_file.setframerate(sample_rate)
    return wave_file


def write_frame(wave_file, freq, duration, sample_rate):
    for i in range(int(duration * sample_rate)):
        l = int(32767.0 * math.cos(freq * math.pi * float(i) / float(sample_rate)))
        r = int(32767.0 * math.cos((freq + 2) * math.pi * float(i) / float(sample_rate)))
        wave_file.writeframesraw(struct.pack('<hh', l, r))

    # wave_file.writeframes('')


def close_wave_file(wave_file):
    wave_file.close()


if __name__ == "__main__":
    sample_rate = 44100.0  # hertz
    t = 2
    wave_file = open_wave_file(sample_rate, 'tow_tiger.wav')
    write_frame(wave_file, reference_table['m1'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m2'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m3'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m1'], t * 0.25, 44100)

    write_frame(wave_file, reference_table['m1'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m2'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m3'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m1'], t * 0.25, 44100)

    write_frame(wave_file, reference_table['m3'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m4'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m5'], t * 0.5, 44100)

    write_frame(wave_file, reference_table['m3'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m4'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m5'], t * 0.5, 44100)

    write_frame(wave_file, reference_table['m5'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m6'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m5'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m4'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m3'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m1'], t * 0.25, 44100)

    write_frame(wave_file, reference_table['m5'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m6'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m5'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m4'], t * 0.125, 44100)
    write_frame(wave_file, reference_table['m3'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m1'], t * 0.25, 44100)

    write_frame(wave_file, reference_table['m2'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['l5'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m1'], t * 0.5, 44100)

    write_frame(wave_file, reference_table['m2'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['l5'], t * 0.25, 44100)
    write_frame(wave_file, reference_table['m1'], t * 0.5, 44100)

    close_wave_file(wave_file)
