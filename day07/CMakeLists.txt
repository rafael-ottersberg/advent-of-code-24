add_library( day07 day07.cpp)

target_include_directories(day07 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day07 TBB::tbb )