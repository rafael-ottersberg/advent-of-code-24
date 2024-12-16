add_library( day20 day20.cpp)

target_include_directories(day20 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day20 TBB::tbb )