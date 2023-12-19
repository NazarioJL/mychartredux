from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class ComponentInfo(BaseSchema):
    component_id: str = Field(alias='componentID')
    name: str
    common_name: str
    units: str


class ReferenceRange(BaseSchema):
    low: float | None
    high: float | None
    display_low: str | None
    display_high: str | None


class ComponentResultInfo(BaseSchema):
    value: str
    numeric_value: float
    reference_range: ReferenceRange
    abnormal_flag_category_value: int
    date_iso: str | None = Field(alias='dateISO')


class ResultComponent(BaseSchema):
    component_info: ComponentInfo
    component_result_info: ComponentResultInfo


class OrderMetadata(BaseSchema):
    authorizing_provider_name: str


class OrderDetail(BaseSchema):
    name: str
    key: str
    order_metadata: OrderMetadata
    result_components: list[ResultComponent]


class GetDetailsResponse(BaseSchema):
    order_name: str
    results: list[OrderDetail]


class ResultGroup(BaseSchema):
    key: str
    result_list: list[str]


class OrganizationLoadMoreInfo(BaseSchema):
    last_group_key: str
    unique_group_count: int


class GetListResponse(BaseSchema):
    organization_load_more_info: dict[str, OrganizationLoadMoreInfo]
    new_result_groups: list[ResultGroup]


class GetListRequest(BaseSchema):
    group_type: int
    last_group_keys: dict[str, str] | None = None
    max_results: int = 50
    search_string: str = ''


class GetDetailsRequest(BaseSchema):
    order_key: str = Field(alias='orderKey')
    organization_id: str = Field(alias='organizationID')
