![img:png](common/github%20封面图.png)
## 引言
这个仓库是一个日志打印封装的Python库，提供了一个名为`LogHandler`的类，用于简化日志记录的配置和使用。该库基于Python标准库中的`logging`模块，提供了一种更便捷的方式来设置日志级别、输出格式和文件分割等功能。

## 具有功能
- 单例模式：通过使用装饰器实现了单例模式，确保`LogHandler`类的实例在整个应用程序中是唯一的。
- 继承`logging.Logger`类：`LogHandler`类继承了`logging.Logger`类，因此可以使用`Logger`类的所有方法和属性。
- 多种日志级别支持：提供了日志级别的映射关系，包括`debug`、`info`、`warning`、`error`和`critical`等级别。
- 日志颜色支持：使用`colorlog`模块实现了日志输出的彩色显示，方便区分不同级别的日志。
- 定时文件分割支持：使用`handlers.TimedRotatingFileHandler`类实现了根据指定时间间隔自动生成日志文件的功能。
- 灵活的日志格式设置：可以通过自定义格式字符串来设置日志的输出格式。
- 屏幕输出和文件输出支持：日志可以同时输出到屏幕和文件中，方便开发和查看日志。

使用示例：

```python
now_time_day = time.strftime("%Y-%m-%d", time.localtime())
INFO = LogHandler(ensure_path_sep(f"\\logs\\info-{now_time_day}.log"), level='info')
ERROR = LogHandler(ensure_path_sep(f"\\logs\\error-{now_time_day}.log"), level='error')
WARNING = LogHandler(ensure_path_sep(f'\\logs\\warning-{now_time_day}.log'))

INFO.info("This is an info message")
ERROR.error("This is an error message")
WARNING.warning("This is a warning message")
```
![img:png](common/实际效果.png)

## END

欢迎各位小伙伴扫码关注 **公众号：小柒测试笔记** ，更多干货可在公众号内获取；
![img:png](common/公众号封面图.png)