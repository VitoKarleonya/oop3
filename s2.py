def count_calls(func):
    def wrapper(*args):
        wrapper.calls += 1
        result = func(*args)
        return result
    wrapper.calls = 0
    return wrapper


class Student:
	tired = 0
	progress = 0
	time = 0

	def __init__(self, name):
		self.name = name
	@count_calls	
	def study(self):
		self.tired += 15
		self.progress += 5
		print(f'{self.name} {self.tired} {self.progress} {self.time}')
		while self.tired > 0:
			s.relax()
        
	
	def days(self):
		while self.progress != 100:
			self.time += 10
			
		
			 
	@count_calls			
	def relax(self):
		if self.tired > 0 and self.progress != 100:
			self.tired -= 5
			self.time += 10
			print(f'{self.name} {self.tired} {self.progress} {self.time}')
		else:
			self.tired = 0


	def done(self):
		if self.progress == 100:
			print('Done')
		else:
			print('Not yet')
  


s = Student("Alice")
while s.progress < 100:
	s.study()
s.done()
calls = s.study.calls + s.relax.calls
print("Всего дней на обучение по такому графику: " , calls)
	

