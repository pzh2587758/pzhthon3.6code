import time

import sys

import os

try:

    import psutil

    psutil_import = True

except ImportError:

    psutil_import = False


class Prog():

    def init(self, iterations, track_time, stream, title,

             monitor, update_interval=None):
        # 迭代次数计数
        self.cnt = 0
        self.title = title
        # 总迭代次数
        self.max_iter = iterations
        # bool 值，指示是否打印总计时间
        self.track = track_time
        self.start = time.time()
        self.end = None
        self.item_id = None
        # 保存预计剩余时间
        self.eta = None
        self.total_time = 0.0
        self.last_time = self.start
        self.monitor = monitor
        # 存储将要使用的输出流
        self.stream = stream
        # 指示进度是否仍在计算中
        self.active = True
        self._stream_out = None
        self._stream_flush = None
        self._check_stream()
        self._print_title()
        # 更新间隔
        self.update_interval = update_interval

        if monitor:
            if not psutil_import:
                raise ValueError('psutil package is required when using'
                                 ' the `monitor` option.')
            else:
                self.process = psutil.Process()
        if self.track:
            self.eta = 1


def update(self, iterations=1, item_id=None, force_flush=False):
    # 更新进度信息（进度条，进度百分比）
    """
    Updates the progress bar / percentage indicator.

    Parameters
    ----------
    iterations : int (default: 1)
        default argument can be changed to integer values
        >=1 in order to update the progress indicators more than once
        per iteration.
    item_id : str (default: None)
        Print an item_id sring behind the progress bar
    force_flush : bool (default: False)
        If True, flushes the progress indicator to the output screen
        in each iteration.

    """
    self.item_id = item_id
    self.cnt += iterations
    self._print(force_flush=force_flush)
    # 确认是否完成，已完成则进行收尾工作
    self._finish()


def _check_stream(self):
    # 确认使用哪个输出流
    """Determines which output stream (stdout, stderr, or custom) to use"""
    if self.stream:
        try:
            if self.stream == 1 and os.isatty(sys.stdout.fileno()):
                self._stream_out = sys.stdout.write
                self._stream_flush = sys.stdout.flush
            elif self.stream == 2 and os.isatty(sys.stderr.fileno()):
                self._stream_out = sys.stderr.write
                self._stream_flush = sys.stderr.flush