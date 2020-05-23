# AWS
resource "aws_lambda_function" "content_server_lambda" {
  function_name = "content_server_lambda"
  handler = ""
  role = ""
  runtime = ""
}

resource "aws_api_gateway_rest_api" "ContentServer" {
  name = "ContentServer"
}
resource "aws_api_gateway_authorizer" "" {
  deployment_id = ""
  rest_api_id = "ContentServer"
  stage_name = ""
  name = ""
}

resource "aws_api_gateway_resource" "root_server" {
  parent_id = "ContentServer"
  path_part = "/"
  rest_api_id = "ContentServer"
}
resource "aws_api_gateway_resource" "web_server" {
  parent_id = "root_server"
  path_part = "/web"
  rest_api_id = "ContentServer"
}

resource "aws_api_gateway_resource" "api_server" {
  parent_id = "root_server"
  path_part = "/api"
  rest_api_id = "ContentServer"
}

resource "aws_api_gateway_method" "" {
  authorization = ""
  http_method = "GET"
  resource_id = "web_server"
  rest_api_id = "ContentServer"
}

resource "aws_api_gateway_method_response" "" {
  http_method = ""
  resource_id = ""
  rest_api_id = ""
  status_code = ""
}

resource "aws_api_gateway_gateway_response" "" {
  response_type = ""
  rest_api_id = ""
}

resource "aws_api_gateway_stage" "development" {
  http_method = ""
  resource_id = ""
  rest_api_id = ""
  status_code = ""
  deployment_id = ""
  stage_name = "development"
}

resource "aws_api_gateway_stage" "production" {
  http_method = ""
  resource_id = ""
  rest_api_id = ""
  status_code = ""
  deployment_id = ""
  stage_name = "production"
}

# Azure
resource "azurerm_function_app" "azure_content_server" {
  app_service_plan_id = ""
  location = ""
  name = ""
  resource_group_name = ""
}

resource "azurerm_api_management" "" {
  location = ""
  name = ""
  publisher_email = ""
  publisher_name = ""
  resource_group_name = ""
  sku_name = ""
}