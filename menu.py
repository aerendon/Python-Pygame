import pygame 

class Opcion:
	ver = False
	ido = 0

	def __init__(self, text, pos, ido):
		self.text = text
		self.pos = pos
		self.set_rect()
		self.draw()
		self.ido = ido

	def retId(self):
		return self.ido

	def draw(self):
		self.set_rend()
		screen.blit(self.rend, self.rect)

	def set_rend(self):
		self.rend = menu_font.render(self.text, True, self.get_color())

	def get_color(self):
		if self.ver:
			return (255, 255, 255)
		else:
			return (100, 100, 100)

	def set_rect(self):
		self.set_rend()
		self.rect = self.rend.get_rect()
		self.rect.topleft = self.pos



pygame.init()
screen = pygame.display.set_mode((480, 320))
menu_font = pygame.font.Font(None, 40)
opciones = [Opcion("NUEVO", (145, 105), 1), Opcion("CARGAR", (145, 155), 2), Opcion("OPCIONES", (145, 205), 3), Opcion("Salir", (145, 255), 4)]

fin = False
pos_click = ()
op = 0

while not fin:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fin = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos_click = pygame.mouse.get_pos()
			for opcion in opciones:
				if opcion.rect.collidepoint(pos_click):
					op = opcion.retId()
					print "opcion seleccionada:", op

					if op == 1:
						screen.fill((0, 0, 100))
						pygame.display.update()
					elif op == 4:
						fin = True


	pygame.event.pump()
	screen.fill((0, 0, 0))

	for opcion in opciones:
		if opcion.rect.collidepoint(pygame.mouse.get_pos()):
			opcion.ver = True
			#print opcion.retId()
		else:
			opcion.ver = False
		opcion.draw()

	pygame.display.update()