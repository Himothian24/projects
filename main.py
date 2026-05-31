import pygame
import sys
import random
from sprites import Player, Alien, Laser

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("OOP Space Shooter")
        self.clock = pygame.time.Clock()
        
        # Instantiate objects
        self.player = Player(self.WIDTH // 2 - 25, self.HEIGHT - 50)
        self.lasers = []
        self.aliens = []
        self.score = 0
        self.running = True

    def spawn_aliens(self):
        # Randomly spawn aliens at the top
        if random.randint(1, 30) == 1:
            x_pos = random.randint(0, self.WIDTH - 40)
            self.aliens.append(Alien(x_pos, -30))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.lasers.append(self.player.shoot())

    def update(self):
        # Move player
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.WIDTH)

        # Update lasers
        for laser in self.lasers[:]:
            laser.update()
            if laser.rect.bottom < 0:
                self.lasers.remove(laser)

        # Update aliens
        for alien in self.aliens[:]:
            alien.update()
            if alien.rect.top > self.HEIGHT:
                self.aliens.remove(alien)
                print(f"An alien escaped! Your score was: {self.score}. Game Over.")
                self.running = False

        # Collision detection (Laser vs Alien)
        for laser in self.lasers[:]:
            for alien in self.aliens[:]:
                if laser.rect.colliderect(alien.rect):
                    self.lasers.remove(laser)
                    self.aliens.remove(alien)
                    self.score += 10
                    break

        # Collision detection (Alien vs Player)
        for alien in self.aliens:
            if alien.rect.colliderect(self.player.rect):
                print(f"You crashed! Final Score: {self.score}")
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0)) # Clear screen with black
        
        # Draw everything
        self.player.draw(self.screen)
        for laser in self.lasers:
            laser.draw(self.screen)
        for alien in self.aliens:
            alien.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.spawn_aliens()
            self.update()
            self.draw()
            self.clock.tick(60) # Lock to 60 FPS

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()