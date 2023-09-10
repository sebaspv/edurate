import fire

class Calculator(object):
  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)