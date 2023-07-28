from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int, default=0)
    var_2 = request.form.get("var_2", type=int, default=0)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
    	if(var_1==0 and var_2==0):
    		result = 0
    	else:
        	result = var_1 / var_2
    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)
#@app.route('/add/<int:num1>/<int:num2>')
#def add(num1,num2):
#    ans=num1+num2
#    #print("your answer is : ", ans)
#    return str(ans)
#
#@app.route('/sub/<int:num1>/<int:num2>')    
#def subtract(num1,num2):
#    ans=num1-num2
#    #print("your answer is : ", ans)
#    return str(ans)
#
#@app.route('/mul/<int:num1>/<int:num2>')
#def multiply(num1,num2):
#    ans=num1*num2
#    #print("your answer is : ", ans)
#    return str(ans)
#
#@app.route('/div/<int:num1>/<int:num2>')
#def divide(num1,num2):
#    ans=num1/num2
#    #print("your answer is : ", ans)
#    return str(ans)

@app.route('/')
def hello():
    return render_template('form.html')

#while True:
#    print("           ")
#    print("1. Add")
#    print("2. Subtract")
#    print("3. Multiply")
#    print("4. Divide")
#    print("0. Exit")
#
#    #choice=int(input("Enter Choice: "))
#    if choice==1:
#        add(num1,num2)
#    if choice==2:
#        subtract(num1,num2)
#    elif choice==3:
#        multiply(num1,num2)
#    elif choice==4:
#        divide(num1,num2)
#    elif choice==0:
#        break
#    else:
#        print("Invalid Choice")
#        continue
#
#print("THANKS")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)