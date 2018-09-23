#!/usr/bin/env python3
import pandas as pd, numpy as np

def main():
    # data_dict = {}
    # data_dict['env_id'] = pd.Categorical(["env_1","env_1","env_1","env_1"])
    # data_dict['net_id'] = pd.Categorical(["actor","critic","actor","critic"])
    # data_dict['opt_id'] = pd.Categorical(["opt_1","opt_2","opt_1","opt_2"])
    # # data_dict['train_loss_epoch_mean'] = np.array([1.23] * 4, dtype='float32')
    # # data_dict['train_loss_epoch_std'] = np.array([1.23] * 4, dtype='float32')
    # data_dict['train_loss_update_mean'] = np.array([1.23] * 4, dtype='float32')
    # data_dict['train_loss_update_std'] = np.array([1.23] * 4, dtype='float32')
    # # data_dict['test_loss_update_mean'] = np.array([1.23] * 4, dtype='float32')
    # # data_dict['test_loss_update_std'] = np.array([1.23] * 4, dtype='float32')
    # # data_dict['train_test_delta_loss_mean'] = np.array([1.23] * 4, dtype='float32')
    # # data_dict['train_test_delta_loss_std'] = np.array([1.23] * 4, dtype='float32')
    # # data_dict['return_all_episodes_mean'] = np.array([np.nan, np.nan, np.nan, 1.23], dtype='float32')
    # # data_dict['return_all_episodes_std'] = np.array([np.nan, np.nan, np.nan, 1.23], dtype='float32')

    # df = pd.DataFrame(data_dict)

    ############################################################################
    # # https://stackoverflow.com/questions/26411829/read-and-write-pandas-dataframe-with-multi-row-and-multi-column-index
    # idx = pd.MultiIndex.from_product([["A", "B"], [1, 2, 3]])
    # col = pd.MultiIndex.from_product([["X", "Y"], ["aa", "bb"]])
    # df = pd.DataFrame(np.random.randint(0, 100, size=(6, 4)), index=idx, columns=col)
    # df.index.names = "name1", "name2"
    # df.columns.names = "NAME1", "NAME2"

    ############################################################################
    # http://pandas.pydata.org/pandas-docs/stable/advanced.html
    arrays = [['bar', 'bar', 'bar', 'baz', 'baz', 'baz'],
              ['one', 'two', 'two', 'one', 'two', 'two'],
              ['a', 'b', 'c', 'a', 'b', 'c']]
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second', 'third'])

    s = pd.Series(np.random.randn(6), index=index)
    print(s)

    ############################################################################
    # print(df)
    # print(df.dtypes)
    # print(df.to_latex())

    # with open('table/table.tex','w') as f:
    #     f.write(df.to_latex())

if __name__ == '__main__':
    main()
