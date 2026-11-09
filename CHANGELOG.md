# PayCalculator AU — Release history / 更新日志

Last updated / 更新日期: 2026-11-09

Release availability is listed for each version. / 每个版本分别标明分发状态。

## 1.4 Beta — Web live · iOS beta distribution in progress / 网页已上线 · iOS Beta 分发进行中

Usability beta: clearer calculation bases, a reorganised Work Value page and consistent scenario comparison. iOS builds 9–11 is distributed through TestFlight only; 1.4 has not been submitted to the App Store.
交互优化 Beta：统一计算口径、整理工作回报页面及方案比较。iOS 版本号 9–11 仅通过 TestFlight 测试，1.4 未提交 App Store。

- Explicit Payslip pay and Annual after tax selectors in Salary and saved comparisons, with a common pay cycle. / 工资页及已保存方案比较明确区分“工资单到手／年度报税后”，工资单比较采用共同发薪周期。
- Work Value separates Annual forecast from Actual records, shows the income basis and groups annual plan inputs. / 工作回报分为年度预测与实际记录，明确收入口径，并集中年度计划设置。
- Temporary waterfall edits can be saved as a separate scenario or discarded; main inputs stay unchanged. / 瀑布图临时修改可保存为独立方案或放弃，不覆盖首页输入。
- Visible Theme label; low-frequency sources, backup and version tools are grouped in More. Calculation notes are collapsed. / 主题入口显示文字；来源、备份、版本等低频工具集中于更多菜单，完整计算说明折叠展示。
- Release build startup and numeric-editing checks retained. Calculation rules and existing data formats are unchanged. / 保留 Release 启动与数字编辑检查；计算规则及原有存储格式不变。
- Build 10 restores the same salary in Salary and Work Value after relaunch, clears outdated forecasts when pay is cleared, and shows the gross annual input used for effective hourly value. / 版本号 10 修复重启后首页与工作回报的工资恢复不一致；清空工资后不再沿用旧预测，并显示有效时薪引用的税前年薪。

Web Beta 1.4 is live. Build 9 was submitted for external TestFlight review on 5 November; build 10 fixes salary restoration, and build 11 also removes a misleading empty-salary message. Latest beta upload and public-group distribution are in progress. 1.4 has not been submitted to the App Store.
网页版 1.4 Beta 已上线。版本号 9 于 11 月 5 日提交 TestFlight 外部测试审核；10 修复工资恢复，11 同时移除清空工资后的误导提示。最新测试包上传与公开组分发进行中。1.4 未提交 App Store。

## 1.3.3 — Submitted on 5 November 2026 / 2026 年 11 月 5 日已送审

Startup-crash fix for affected devices on iOS 27.0.1. The affected user confirmed TestFlight build 8 opens normally on the same iPhone 17 Pro.
修复部分 iOS 27.0.1 设备启动闪退；用户已确认 TestFlight 版本号 8 在原故障 iPhone 17 Pro 上正常打开。

- Bounds nested SwiftUI screen metadata; calculation rules and saved-data formats are unchanged. / 缩短 SwiftUI 界面类型嵌套；计算规则及存储格式不变。

Submitted with automatic App Store release after approval. This records the 5 November submission; check the App Store for current availability. Separate from the 1.4 usability beta.
提交时设置为获批后自动发布；此处记录 11 月 5 日送审事件，当前可用版本请查看 App Store。与 1.4 交互优化 Beta 分开。

## 1.3.2 — Released on the App Store / App Store 已发布

Version 1.3.2 (build 7) was approved and released. A subsequent startup crash reported on iOS 27.0.1 is addressed by the separate 1.3.3 patch.
1.3.2（版本号 7）已获批并发布；后续发现的 iOS 27.0.1 启动闪退由独立的 1.3.3 修复版处理。

- Includes the language and date-display fixes from 1.3.1. / 包含 1.3.1 的语言与日期显示修复。
- Wide windows place inputs and results in columns; narrow windows keep a compact layout. / 宽窗口分栏显示输入与结果，窄窗口保留紧凑布局。
- Number fields preserve decimals and incomplete edits without reformatting while you type. / 数字输入保留小数和编辑过程，不在输入途中强制重新格式化。
- Built with the iOS 27.2 SDK. Checked iPhone Duo outer and inner displays, state preservation, standard iPhone and iPad portrait/landscape layouts. / 使用 iOS 27.2 SDK 构建；已检查 Duo 内外屏、切换时的数据保留，以及标准 iPhone 与 iPad 横竖屏布局。
- Added 30 real screenshots across the iPhone, iPad 13-inch and iPhone Duo groups in English and Simplified Chinese, covering all five tabs. / 为 iPhone、13 英寸 iPad 及 iPhone Duo 提供中英文共 30 张真实新截图，覆盖五个标签页。
- Calculation rules are unchanged. / 计算规则保持不变。

See 1.3.3 for the startup-crash fix and its distribution status.
启动闪退修复及分发状态请参阅 1.3.3。

## Web Beta 1.3.2 — Available on the web / 网页已上线

Aligned version labels, narrow-screen layouts and direct App Store installation, with a separate TestFlight option.
统一版本标识、改善窄屏布局，提供正式 App Store 下载及独立 TestFlight 入口。

- Aligned version labels and improved narrow-screen layouts. / 统一版本标识并改善窄屏布局。
- Direct App Store installation with a separate TestFlight beta option. / 提供正式 App Store 下载，并保留独立 TestFlight 测试入口。

Web data stays in this browser. Local reminders and native backup/restore remain app-only.
网页数据存于当前浏览器；本地提醒和原生备份恢复仅 App 支持。

## 1.3.1 — Available in TestFlight / 已开放 TestFlight

English and Chinese localisation fixes. No new features or changes to calculation rules.
修复中英文界面本地化问题，无新增功能或计算规则变更。

- Language changes now refresh reusable labels, pay-period selectors, state names and source cards consistently. / 切换语言时同步刷新周期选择、州名、来源卡片等组件，避免残留上一种语言。
- Date pickers and displayed dates follow the selected app language instead of the device region. / 日期控件及日期显示跟随应用语言，避免英文界面出现中文年月日。
- Refined ordinary interface translations while preserving professional terms, brand names and Big 4 slogans. / 完善普通界面文案翻译，保留专业术语、品牌名称及 Big 4 slogan。

Version 1.3.1 (build 6) is a localisation-only maintenance update. Available to external testers; not released on the App Store.
1.3.1（版本号 6）仅修复本地化问题。已开放外部测试；此版本尚未在 App Store 发布。

## 1.3 — Available on the App Store / App Store 已上线

A clearer view of your pay, your time and your earnings benchmark.
更清晰地看见工资、时间投入与全国工资参考。

- A dedicated Work Value tab: effective net hourly value, contract-hour comparison and paid idle-time value. / 新增工作回报 tab：有效税后时薪、合同工时对比及有薪摸鱼时间价值。
- Annual plans for idle time, paid annual and sick leave; purchased leave syncs from Salary. Daily records replace planned work hours without double counting. / 支持年度摸鱼、带薪年假及病假计划；购买年假同步工资页，实际记录替换对应计划，避免重复计算。
- Daily idle-time and unpaid-overtime records, with optional local reminders at the end of the working day. / 每日记录摸鱼及无额外计薪加班，可选下班本地提醒。
- National and state public holidays follow your work state and financial year. Deducts only overlapping scheduled hours; weekday substitutes count and weekend dates are not deducted twice. / 按工作所在州及财年自动套用全国和本州公共假期，仅扣除排班重合时间，工作日补休计入，周末日期不重复扣除。
- Browse public holidays across all states and supported financial years, with regional applicability, source links and estimated future dates clearly identified. / 浏览各州及全部支持财年的公共假期，标明地区适用范围、官方来源和预计未来日期。
- The salary example uses ABS national median weekly employee earnings, annualised and excluding employer super. An indicative base-pay percentile includes FY reference periods and linked methodology. / 示例工资采用 ABS 全国雇员周薪中位数年化参考值，明确不含雇主 Super；基本工资百分位估算附财年参考期及来源说明。
- Consistent branding and toolbar options across tabs. Theme and colour settings group standard colours and Big 4 palettes, with light, dark and system appearance. / 统一各 tab 的品牌及工具栏；主题与颜色菜单分组标准配色、Big 4 配色及浅色、深色、跟随系统模式。
- In-app links to release history, email feedback and signed-in GitHub feature requests or bug reports. / 应用内加入更新日志、邮件留言及登录 GitHub 提交需求或问题的入口。
- A direct “How it’s calculated” view reconciles annual cash pay, purchased leave, bonus, super sacrifice, taxable income, deductions, tax and HELP. / 结果卡新增“怎么算的”，展示年度现金工资、购买年假、奖金、额外 Super、应税收入、扣除、税费与 HELP 的计算路径。
- Compact active-setting chips link to bonus, leave, HELP, extra super, deductions and Medicare/family settings. / 用简洁标签显示影响结果的已启用设置，点击可进入奖金、年假、HELP、额外 Super、扣除与医保／家庭设置。
- Work Value includes same-scale hourly comparisons and a scheduled-hours breakdown, with unpaid overtime shown separately. Annual records follow revised schedules consistently. / 工作回报新增同一比例尺的时薪对比与排班工时分解，另列无额外计薪加班；调整排班后年度记录按同一工时口径计算。
- Saving a daily check-in shows effective hourly value, paid idle-time value and planned goal allocation; actual savings remain separately confirmed. / 保存每日记录后显示有效时薪、有薪摸鱼时间价值与计划目标分配；实际储蓄仍需另行确认。
- Tax source and applicability notes are consistent across calculator views. Holiday source links are grouped and deduplicated with the bundled dataset date, instead of repeating in every holiday card. / 计算页面统一税务来源与适用范围说明；公共假期来源集中去重并显示本地资料日期，去掉每张假期卡片重复的来源链接。
- National base-pay rankings show an approximate top/bottom employee percentage alongside the original percentile, preserving bounds and the statistical comparison population. / 全国基本工资排名同时显示直观的雇员前／后百分比与原百分位，保留估算边界和统计比较范围。
- Tax details add taxable-income and take-home cash waterfall charts without replacing the table. Charts scroll horizontally and offer an enlarged view with zoom and landscape support. / 税务明细新增应税收入与现金到手双路径瀑布图，保留原有表格；支持横向滚动、全屏放大、缩放及横屏查看。
- Work Value uses consistent “working day” terminology in English and Chinese. / 工作回报统一使用中英文“工作日／working day”表述。
- The result card defaults to regular PAYG payslip estimates, with a separate switch for annual after-tax-return estimates. / 结果卡默认呈现正常 PAYG 工资单估算，通过独立开关切换年度报税后估算。

Version 1.3 (build 5) was released on the App Store on 3 November 2026. TestFlight distribution remains separate.
1.3（版本号 5）于 2026 年 11 月 3 日在 App Store 上线；TestFlight 分发另行管理。

## 1.2 — Submitted build / 已提交版本

Salary scenarios, deductions and a more consistent everyday calculator.
工资方案、税务扣除及更一致的日常计算体验。

- A dedicated Tax deduction tab, synced with Salary and HELP / HECS calculations. / 独立 Tax deduction 页面，与工资及 HELP / HECS 计算同步。
- Save, compare and share salary scenarios; an optional HELP balance caps estimated annual repayments. / 保存、比较及分享工资方案；可选 HELP 余额限制年度还款估算。
- Clearer super inclusion controls, configurable employer Super Guarantee rate and financial-year labels. / 更清晰的包含 Super 开关、可调整的雇主 Super Guarantee 比例及财年标识。
- Annual, monthly, fortnightly and weekly take-home estimates appear together in the main result card. / 主结果卡同时呈现年、月、两周和每周到手金额。
- Refreshed app branding, Purple and Green themes, bilingual labels and a keyboard Done control. / 更新应用品牌、Purple 与 Green 主题、双语标签及数字键盘完成按钮。

Listed as a submitted build, not confirmation of App Store availability. This entry summarises the version's features; it is not a claim that every feature first appeared in 1.2.
此处表示已提交版本，不代表已在 App Store 上架；本条为版本功能概要，不表示所有功能均首次加入 1.2。

## 1.1.1 — Historical test build / 历史测试版本

Quicker salary adjustment and clearer tax-year tables.
更快捷的工资调整与财年税率表。

- A salary slider under the gross-pay input. / 税前工资输入下方加入工资滑动条。
- Updated tax-table thresholds when switching financial years. / 切换财年时更新税率表的收入门槛。
- Updated logo and colour integration. / 更新 logo 与应用配色融合。

## 1.1 — Initial test build / 初始测试版本

The first TestFlight calculator build.
首个 TestFlight 计算器版本。

- Australian salary, tax, Medicare, super and HELP / HECS estimates across supported financial years. / 支持不同财年的澳大利亚工资、所得税、Medicare、Super 及 HELP / HECS 估算。
- Purchased annual leave and bonus settings, including a one-off bonus paid in a selected month. / 购买额外年假及奖金设置，支持指定月份一次性奖金。
- A tax-rate explorer, bilingual interface and selectable colour themes. / 税率探索、双语界面及可切换配色主题。
