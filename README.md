PyTorch1.3

```
├── data/
│   ├── dataset.py
│   └── get_data.sh
├── models/
│   ├── BasicModule.py
│   └── ResNet34.py
└── utils/
│   └── visualize.py
├── config.py
├── main.py
├── README.md
```
data/：数据和相关操作，如数据预处理、dataset实现等
models/：模型定义，一个模型对应一个文件
utils/：可能用到的工具函数，如可视化工具
config.py：配置文件，所有可配置的变量都集中在此
main.py：主文件，训练和测试程序的入口，可通过不同的命令来指定不同的操作和参数
README.md：提供程序的必要说明