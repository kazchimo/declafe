import pandas as pd

from declafe.agg_feature_gen.GroupBy import groupby

test_df = pd.DataFrame(
    {
        "a": list(range(1, 251)) * 4,
        "b": list(range(1001, 2001)),
        "c": list(range(2001, 3001))
    })


class TestGen:

  def test_agg(self):
    by_a = groupby("a")
    b_agg = by_a.count.last.target("b")
    c_agg = by_a.count.target("c")
    agg = b_agg + c_agg
    res = agg.gen(test_df)

    assert res.equals(
        test_df.groupby("a").agg(
            count_of_b=pd.NamedAgg("b", "count"),
            last_of_b=pd.NamedAgg("b", "last"),
            count_of_c=pd.NamedAgg("c", "count")))