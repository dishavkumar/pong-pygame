import pygame
import random

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

PADDLE_SPEED = 0.6
BALL_SPEED = 0.4


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 0

    def move(self, delta_time):
        self.rect.y += self.speed * delta_time
        # Keep paddle inside the screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20)
        self.reset()

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.vel_x = random.choice([-1, 1]) * BALL_SPEED
        self.vel_y = random.choice([-1, 1]) * BALL_SPEED

    def move(self, delta_time, paddle1, paddle2):
        self.rect.x += self.vel_x * delta_time
        self.rect.y += self.vel_y * delta_time

        # Bounce on top/bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.vel_y *= -1

        # Bounce on paddles
        if self.rect.colliderect(paddle1.rect) and self.vel_x < 0:
            self.vel_x *= -1
            self.rect.left = paddle1.rect.right
        if self.rect.colliderect(paddle2.rect) and self.vel_x > 0:
            self.vel_x *= -1
            self.rect.right = paddle2.rect.left

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_WHITE, self.rect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

        self.paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - 50)
        self.paddle2 = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2 - 50)
        self.ball = Ball()

        self.font = pygame.font.SysFont("Consolas", 36)
        self.score1 = 0
        self.score2 = 0
        self.running = True
        self.started = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.paddle1.speed = -PADDLE_SPEED
                if event.key == pygame.K_s:
                    self.paddle1.speed = PADDLE_SPEED
                if event.key == pygame.K_UP:
                    self.paddle2.speed = -PADDLE_SPEED
                if event.key == pygame.K_DOWN:
                    self.paddle2.speed = PADDLE_SPEED
                if event.key == pygame.K_SPACE:
                    self.started = True

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    self.paddle1.speed = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.paddle2.speed = 0

    def update(self, delta_time):
        if not self.started:
            return

        self.paddle1.move(delta_time)
        self.paddle2.move(delta_time)
        self.ball.move(delta_time, self.paddle1, self.paddle2)

        # Scoring
        if self.ball.rect.left <= 0:
            self.score2 += 1
            self.ball.reset()
        if self.ball.rect.right >= SCREEN_WIDTH:
            self.score1 += 1
            self.ball.reset()

    def draw(self):
        self.screen.fill(COLOR_BLACK)

        if not self.started:
            text = self.font.render("Press SPACE to Start", True, COLOR_WHITE)
            self.screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        else:
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            self.ball.draw(self.screen)

            # Draw scores
            score_text = self.font.render(f"{self.score1} - {self.score2}", True, COLOR_WHITE)
            self.screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, 30)))

        pygame.display.flip()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60)
            self.handle_events()
            self.update(delta_time)
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    Game().run()
