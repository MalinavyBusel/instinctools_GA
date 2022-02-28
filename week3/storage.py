class AppendToLockedError(PermissionError):
    pass


class LogicalWarning(Warning):
    pass


class Storage:
    def __init__(self, *args):
        self.data = [*args]
        self.is_appendable = False

    def __enter__(self):
        if self.is_appendable:
            raise LogicalWarning('You are trying to unlock an already unlocked storage.'
                                 ' Please, check your code for logical mistakes.')
        else:
            self.unlock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock()

    def lock(self):
        self.is_appendable = False

    def unlock(self):
        self.is_appendable = True

    def show(self):
        return self.data.copy()

    def append(self, *args):
        if self.is_appendable:
            appended = [*args]
            self.data += appended
        else:
            raise AppendToLockedError('You are trying to append data to '
                                      'a locked storage. To unlock it, use '
                                      '.unlock() method.')


if __name__ == '__main__':
    my_st = Storage('a', 'b', 'c')
    # my_st.append('d', 'e', 'f')
    my_st.unlock()
    my_st.append('d', 'e', 'f')
    print(my_st.show())
    with my_st as stor:
        stor.append('d', 'e', 'f')
