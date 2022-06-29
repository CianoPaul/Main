from django.db import models

class Item(models.Model):
	sname = models.CharField(max_length=40)
	fname = models.CharField(max_length=50)
	mname = models.CharField(max_length=50)
	age = models.TextField(default="")
	add = models.TextField(default="")
	contact = models.TextField(default="")
	disease = models.TextField(default="")
	specifydisease = models.TextField(default="")
	plan = models.TextField(default="")
	total = models.TextField(default="")
	
	customerID = models.TextField(default="",primary_key=True)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#productID = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.customerID
	
class ExercisePlan(models.Model):
	intensity = models.TextField(default="")
	focus = models.TextField(default="")
	Duration = models.TextField(default="")
	
	planID = models.TextField(default="",primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	customer_plan = models.OneToOneField(Item, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.planID

class Program(models.Model):
	Diet Plan = models.TextField(default="")
	Trainer = models.TextField(default="")
	Duration = models.TextField(default="")
	
	programID = models.TextField(default="",primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	prg_prd = models.ManyToManyField(ExercisePlan, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.programID
	
class Products(models.Model):
	focus = models.TextField(default="")
	supplements = models.TextField(default="")
	clothing = models.TextField(default="")
	extras = models.TextField(default="")
	productID = models.TextField(default="",primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)
	program_product = models.ManyToManyField(Program, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.productID
	
class Review(models.Model):
	feedback = models.TextField(default="")
	concern = models.TextField(default="")
	complaints = models.TextField(default="")
	
	reviewID = models.TextField(default="",primary_key=True)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#productID = models.ForeignKey(Item, on_delete=models.CASCADE)
	review_item = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.reviewID
	
