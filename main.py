from chip8 import cpu

if __name__ == "__main__":
    chip8emu = cpu(640, 320)
    chip8emu.main()