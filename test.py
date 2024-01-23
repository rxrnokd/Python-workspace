import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hydrogen Atom Simulator")

class HydrogenAtomSimulator:
    font_small = pygame.font.Font(None, 18)

    def __init__(self):
        self.clock = pygame.time.Clock()

        self.nucleus_radius = 15
        self.orbit_radius = [150, 200, 250]
        self.orbit_count = len(self.orbit_radius)
        self.current_orbit = 0
        self.prev_orbit = 0
        self.angle = 0

        self.electron_speed = 0.5  # Slowed down the speed
        self.transitioning = False
        self.transition_progress = 0
        self.transition_duration = 30  # Frames for the transition

        self.wave_amplitude = 10
        self.wave_frequency = 0.1

        self.run_simulation()

    def calculate_electron_position(self):
        x = WIDTH // 2 + self.orbit_radius[self.current_orbit] * math.cos(math.radians(self.angle))
        y = HEIGHT // 2 + self.orbit_radius[self.current_orbit] * math.sin(math.radians(self.angle))
        return x, y

    def switch_orbit(self, direction):
        self.prev_orbit = self.current_orbit
        self.current_orbit = (self.current_orbit + direction) % self.orbit_count
        self.transitioning = True
        self.transition_progress = 0

    def run_simulation(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.switch_orbit(1)  # Switch to the right orbit
                    elif event.key == pygame.K_DOWN:
                        if self.current_orbit > 0:
                            self.switch_orbit(-1)  # Switch to the inner orbit

            # Update electron position
            self.angle += self.electron_speed
            electron_position = self.calculate_electron_position()

            # Draw background
            screen.fill(WHITE)

            # Draw nucleus (proton)
            pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), self.nucleus_radius)

            # Draw orbits and display quantum number
            for i, radius in enumerate(self.orbit_radius):
                pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), radius, 2)

                # Display quantum number inside each orbit
                quantum_number = i + 1
                text_render = HydrogenAtomSimulator.font_small.render(f"n={quantum_number}", True, BLACK)
                text_position = (WIDTH // 2 - 15, HEIGHT // 2 - radius + 5)
                screen.blit(text_render, text_position)

            # Draw electron
            pygame.draw.circle(screen, BLUE, (int(electron_position[0]), int(electron_position[1])), 8)

            # Draw electromagnetic wave representation during transition
            if self.transitioning:
                self.draw_wave_transition(electron_position)

            # Display potential energy next to the electron
            if not self.transitioning:
                self.display_potential(electron_position)

            pygame.display.flip()
            self.clock.tick(60)

            # Check for transition progress
            if self.transitioning:
                self.transition_progress += 1
                if self.transition_progress >= self.transition_duration:
                    self.transitioning = False

        pygame.quit()
        sys.exit()

    def draw_wave_transition(self, position):
        wave_x = position[0]  # Initialize wave_x without changing its sign
        wave_y = position[1]

        transition_factor = self.transition_progress / self.transition_duration
        transition_radius = int(self.orbit_radius[self.prev_orbit] +
                                (self.orbit_radius[self.current_orbit] - self.orbit_radius[self.prev_orbit]) *
                                transition_factor)

        arrowhead_size = 8

        for i in range(-100, 100):
            wave_point_x = int(wave_x + i)
            wave_point_y = int(wave_y + self.wave_amplitude * math.sin(self.wave_frequency * i))

            # Adjust the direction of the wave based on the transition
            if self.prev_orbit < self.current_orbit:
                wave_point_x -= int(self.orbit_radius[self.current_orbit])
            else:
                wave_point_x += int(self.orbit_radius[self.prev_orbit])

            pygame.draw.circle(screen, GREEN, (wave_point_x, wave_point_y), 2)

            # Draw arrowhead at the right end
            if i == 99:
                pygame.draw.polygon(screen, GREEN, [(wave_point_x, wave_point_y - arrowhead_size),
                                                     (wave_point_x, wave_point_y + arrowhead_size),
                                                     (wave_point_x + arrowhead_size * 2, wave_point_y)])

    def display_potential(self, position):
        quantum_number = self.current_orbit + 1
        potential_energy = -13.6 / (quantum_number**2)  # Simple potential energy calculation
        text_render = HydrogenAtomSimulator.font_small.render(f"V={potential_energy:.2f} eV", True, BLACK)
        text_position = (int(position[0]) + 15, int(position[1]) - 20)
        screen.blit(text_render, text_position)

if __name__ == "__main__":
    simulator = HydrogenAtomSimulator()
