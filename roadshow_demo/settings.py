import pygame
import numpy as np

white = (255,255,255)
cyan = (0,200,200)


#initial
pygame.init()
pygame.display.set_caption("MOTION GAME!")

# Display for fullscreen
display_width = pygame.display.Info().current_w
display_height = pygame.display.Info().current_h

# for fullscreen
#screen = pygame.display.set_mode([display_width, display_height], pygame.FULLSCREEN | pygame.NOFRAME | pygame.HWSURFACE, 32)
screen = pygame.display.set_mode([display_width, display_height])

clock = pygame.time.Clock()

leg_label1 = np.array([83.65840977699015,
                        17.626292629082677,
                        156.55267426830184,
                        89.39508522238597,
                        99.8315555417711,
                        139.5958684915879,
                        80.82267053256157,
                        14.600449140468962,
                        170.30105914869307,
                        106.16452451475014,
                        79.55670656179112,
                        172.23372008576416,
                        172.23372008576416,
                        87.95756309434518])

leg_label2 = np.array([86.69679535222944,
                        12.424778235029741,
                        167.02206352080853,
                        90.22761341372716,
                        96.6444108264961,
                        171.73089007435505,
                        78.50599177655495,
                        14.119431730407616,
                        159.1229352383847,
                        104.62057578935602,
                        109.19032911395873,
                        119.15079560583172,
                        119.15079560583172,
                        81.22515494325414])

manse_label1 = np.array([80.53458518445224,
                            84.376594027861,
                            86.89882436488416,
                            96.62547766886149,
                            88.59657286532767,
                            175.09593024152815,
                            84.92202728260551,
                            90.66339064815561,
                            82.72740995911713,
                            97.93598068903847,
                            89.35024411197374,
                            173.99171875775852,
                            173.99171875775852,
                            88.65539184204688])

manse_label2 = np.array([83.99703113249197,
                            159.05262326194162,
                            159.20922884772486,
                            96.89462639067158,
                            85.19362455079239,
                            173.90994708603586,
                            87.06228460539147,
                            157.5747415180131,
                            156.1704288963813,
                            92.05029158321538,
                            91.08181594326905,
                            174.55676356986686,
                            174.55676356986686,
                            80.38108652700386])
