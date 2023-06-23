# FaceYourBug
Exception handler written in Python that shows a picture giving the most representative description of your bug

## Usage example

```
from supervisor import Dian0Supervisor

# Create an instance of the custom exception handler
custom_excepthook = Dian0Supervisor()
# Set the custom exception handler as the excepthook
sys.excepthook = custom_excepthook
```

From now on all the errors will trigget the custom execption