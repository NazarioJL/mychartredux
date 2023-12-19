from typing import Protocol

from src.mychartredux.models.mychart import GetListRequest
from src.mychartredux.models.mychart import GetListResponse


class MyChartTestResultsClient(Protocol):
    def get_list(self, request: GetListRequest) -> GetListResponse:
        pass

    def get_details(self, request: GetListRequest) -> GetListResponse:
        pass


class MyChartTestResultsClientHTTP(MyChartTestResultsClient):
    def get_list(self, request: GetListRequest) -> GetListResponse:
        raise NotImplementedError

    def get_details(self, request: GetListRequest) -> GetListResponse:
        raise NotImplementedError
