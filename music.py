import pygame

pygame.mixer.init()

# Hàm để chơi nhạc
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 để lặp lại nhạc

# Hàm để tắt/bật nhạc
def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Hàm để vẽ thanh điều chỉnh âm thanh
def draw_volume_bar(screen, volume, bar_width=200, bar_height=20, bar_color=(255, 0, 0), bar_background_color=(100, 100, 100)):
    pygame.draw.rect(screen, bar_background_color, (10, 10, bar_width, bar_height))
    pygame.draw.rect(screen, bar_color, (10, 10, int(bar_width * volume), bar_height))

# Hàm để lấy giá trị âm lượng từ thanh điều chỉnh
def get_volume_from_mouse(pos, bar_width):
    x, _ = pos
    volume = max(0, min(1, (x - 10) / bar_width))  # Giới hạn giá trị âm lượng từ 0 đến 1
    return volume

# Main game loop
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Volume Control")

    volume = 0.5  # Giá trị mặc định của âm lượng

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    toggle_music()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 210 and 10 <= event.pos[1] <= 30:
                    volume = get_volume_from_mouse(event.pos, 200)
                    pygame.mixer.music.set_volume(volume)
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Kiểm tra nếu nút chuột trái được nhấn
                    if 10 <= event.pos[0] <= 210 and 10 <= event.pos[1] <= 30:
                        volume = get_volume_from_mouse(event.pos, 200)
                        pygame.mixer.music.set_volume(volume)

        screen.fill((255, 255, 255))
        draw_volume_bar(screen, volume)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
