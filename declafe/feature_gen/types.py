from typing import Union, Literal

DTypes = Union[Literal["category"], Literal["int8"], Literal["int16"],
               Literal["int32"], Literal["int64"], Literal["float16"],
               Literal["float32"], Literal["float64"], Literal["bool"],
               Literal["datetime64[ns]"], Literal["timedelta[ns]"],
               Literal["object"], Literal["uint8"], Literal["uint16"],
               Literal["uint32"], Literal["uint64"]]
