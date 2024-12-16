add_library( day13 day13.cpp)

target_include_directories(day13 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day13 TBB::tbb )