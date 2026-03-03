#!/bin/bash
# 检查项目状态脚本
# 用于每日定时检查项目进展

APP_TOKEN="MWT8bBCR3ai80QsLwjwc3ACvnJg"
TABLE_ID="tblmlBjhA1DDsZd4"

# 获取 tenant_access_token
get_token() {
  APP_ID="cli_a92eb99092781bc7"
  APP_SECRET="${FEISHU_APP_SECRET}"
  
  curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
    -H "Content-Type: application/json" \
    -d "{\"app_id\": \"$APP_ID\", \"app_secret\": \"$APP_SECRET\"}" | \
    grep -o '"tenant_access_token":"[^"]*"' | sed 's/.*"tenant_access_token":"\([^"]*\)".*/\1/'
}

# 查询所有项目
fetch_projects() {
  TOKEN=$(get_token)
  curl -s -X GET "https://open.feishu.cn/open-apis/bitable/v1/apps/$APP_TOKEN/tables/$TABLE_ID/records?page_size=500" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json"
}

# 检查意向阶段超过7天的项目
check_intent_timeout() {
  echo "检查意向阶段超时项目..."
  # 实际逻辑由AI实现
}

# 检查商谈中超过14天的项目
check_negotiation_timeout() {
  echo "检查商谈中超时项目..."
  # 实际逻辑由AI实现
}

# 主函数
main() {
  echo "项目状态检查开始: $(date)"
  fetch_projects
  echo "项目状态检查结束: $(date)"
}

main "$@"
